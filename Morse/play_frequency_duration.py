import numpy as np
import soundfile as sf
from scipy.signal import find_peaks
from scipy.fftpack import fft

# Morse Code Dictionary
INTERNATIONAL_MORSE_CODE = {'A': '.-',
                            'B': '-...',
                            'C': '-.-.',
                            'D': '-..',
                            'E': '.',
                            'F': '..-.',
                            'G': '--.',
                            'H': '....',
                            'I': '..',
                            'J': '.---',
                            'K': '-.-',
                            'L': '.-..',
                            'M': '--',
                            'N': '-.',
                            'O': '---',
                            'P': '.--.',
                            'Q': '--.-',
                            'R': '.-.',
                            'S': '...',
                            'T': '-',
                            'U': '..-',
                            'V': '...-',
                            'W': '.--',
                            'X': '-..-',
                            'Y': '-.--',
                            'Z': '--..',

                            '1': '.----',
                            '2': '..---',
                            '3': '...--',
                            '4': '....-',
                            '5': '.....',
                            '6': '-....',
                            '7': '--...',
                            '8': '---..',
                            '9': '----.',
                            '0': '-----'
                            }
# Invert the dictionary
MORSE_CODE_DICT = {value: key for key, value in INTERNATIONAL_MORSE_CODE.items()}

# Frequency in Hz of the sound, duration in seconds
DOTS = (700, 0.100)
DASHES = (700, 0.300)

PAUSE_BETWEEN_DASH_DOT = (0, 0.100)
PAUSE_BETWEEN_LETTERS = (0, 0.300)
PAUSE_BETWEEN_WORDS = (0, 0.700)

SAMPLE_RATE = 44100


def decode_morse_code_sound_file():
    # Load the audio file
    audio, _ = sf.read('sound.wav')

    # find silence
    silence = np.where(audio == 0)[0]
    silence_diff = np.diff(silence)

    change_indices = np.where(silence_diff[:-1] != silence_diff[1:])[0] + 1

    # add 0 first indexes
    change_indices = np.insert(change_indices, 0, 0)
    differences = np.diff(change_indices)

    code = ''
    for i in range(len(differences)):
        if differences[i] == 70:
            code += '.'
        elif differences[i] == 210:
            code += '-'
        else:
            code += ' '

    print(code)
    return code


def generate_sound(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    if frequency == 0:
        signal = np.zeros_like(t)
    else:
        # generate sinusoidal audio signal
        signal = 0.5 * np.sin(2 * np.pi * frequency * t)
    return signal


def write_code_file(freq_duration_pairs):
    audio = np.array([])

    # generate audio for each (frequency, duration) pair
    for freq, duration in freq_duration_pairs:
        sound = generate_sound(freq, duration, SAMPLE_RATE)
        audio = np.concatenate((audio, sound))

    # ensure that highest value is in 16-bit range
    audio *= 32767 / np.max(np.abs(audio))

    # convert to 16-bit data
    audio = audio.astype(np.int16)

    # save as wav file
    sf.write('sound.wav', audio, SAMPLE_RATE)


def code_frequencies_morse_code(morse_code):
    frequency_pairs = []
    for letter in morse_code:
        for dot_dash in letter:
            match dot_dash:
                case '.':
                    frequency_pairs.append(DOTS)
                    frequency_pairs.append(PAUSE_BETWEEN_DASH_DOT)
                case '-':
                    frequency_pairs.append(DASHES)
                    frequency_pairs.append(PAUSE_BETWEEN_DASH_DOT)
                case ' ':
                    frequency_pairs.append(PAUSE_BETWEEN_WORDS)
                case _:
                    raise ValueError(f'Invalid character {letter} in morse code')
        frequency_pairs.append(PAUSE_BETWEEN_LETTERS)

    return frequency_pairs


def encode_morse_code(message):
    morse_code = []
    for word in message.upper().split():
        for letter in word:
            morse_code.append(INTERNATIONAL_MORSE_CODE[letter])
        morse_code.append(' ')
    return morse_code


if __name__ == '__main__':
    while True:
        message_to_code = input('type quit to end!  Message? ')
        if message_to_code == 'quit':
            break

        code = encode_morse_code(message_to_code)
        frequencies_duration = code_frequencies_morse_code(code)
        write_code_file(frequencies_duration)
        print(frequencies_duration)

        decoded = decode_morse_code_sound_file()
        print(decoded)
