import numpy as np
import soundfile as sf
import types

const = types.SimpleNamespace()
const.DOT = '.'
const.DASH = '_'
const.SPACE = ' '

# Morse Code Dictionary
INTERNATIONAL_MORSE_CODE = {'A': '._',
                            'B': '_...',
                            'C': '_._.',
                            'D': '_..',
                            'E': '.',
                            'F': '.._.',
                            'G': '__.',
                            'H': '....',
                            'I': '..',
                            'J': '.___',
                            'K': '_._',
                            'L': '._..',
                            'M': '__',
                            'N': '_.',
                            'O': '___',
                            'P': '.__.',
                            'Q': '__._',
                            'R': '._.',
                            'S': '...',
                            'T': '_',
                            'U': '.._',
                            'V': '..._',
                            'W': '.__',
                            'X': '_.._',
                            'Y': '_.__',
                            'Z': '__..',

                            '1': '.____',
                            '2': '..___',
                            '3': '...__',
                            '4': '...._',
                            '5': '.....',
                            '6': '_....',
                            '7': '__...',
                            '8': '___..',
                            '9': '____.',
                            '0': '_____'
                            }

# Invert the dictionary to be able to use morse code as keys
MORSE_CODE_DICT = {value: key for key, value in INTERNATIONAL_MORSE_CODE.items()}

MAX_CODE_LENGTH = max([len(code) for code in MORSE_CODE_DICT.keys()])
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
    # append end of dash or dot
    differences = np.append(differences, 4410)
    # append end of letter
    differences = np.append(differences, 17640)

    code = ''
    letter_code = []
    for i in range(len(differences)):
        if differences[i] == 0:
            continue
        if differences[i] == 70:
            code += const.DOT
        elif differences[i] == 210:
            code += const.DASH
        elif differences[i] == 4410:
            # end of dot or dash
            pass
        elif differences[i] == 17640:
            # end of a letter
            letter_code.append((MORSE_CODE_DICT[code], code))
            code = ''
        else:
            # end of a word
            code = ''
            letter_code.append((' ', ' '))

    return letter_code


def generate_sound(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    if frequency == 0:
        signal = np.zeros_like(t)
    else:
        # generate sin audio signal
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
                case const.DOT:
                    frequency_pairs.append(DOTS)
                    frequency_pairs.append(PAUSE_BETWEEN_DASH_DOT)
                case const.DASH:
                    frequency_pairs.append(DASHES)
                    frequency_pairs.append(PAUSE_BETWEEN_DASH_DOT)
                case const.SPACE:
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


def pretty_print(decoded):

    str_letters = ''
    str_codes = ''
    letter_spaces = (MAX_CODE_LENGTH - 1) * ' '
    for letter, code in decoded:
        str_letters += letter + letter_spaces
        str_codes += code.ljust(MAX_CODE_LENGTH, ' ')

    print()
    print(str_letters)
    print(str_codes)


if __name__ == '__main__':
    while True:
        message_to_code = input('type quit to end!  Message? ')
        if message_to_code == 'quit':
            break

        print()
        code = encode_morse_code(message_to_code)
        frequencies_duration = code_frequencies_morse_code(code)
        write_code_file(frequencies_duration)
        print(frequencies_duration)

        decoded = decode_morse_code_sound_file()
        pretty_print(decoded)

