from pydub import AudioSegment
from pydub.playback import play
import numpy as np
from scipy.io.wavfile import write
import scipy.io.wavfile as wav
from scipy.signal import find_peaks
from time import sleep
import librosa

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
# Frequency in Hz of the sound, duration in ms
DOTS = (700, 100)
DASHES = (700, 300)
# Pauses in seconds
PAUSE_BETWEEN_DASH_DOT = 0.1
PAUSE_BETWEEN_LETTERS = 0.300
PAUSE_BETWEEN_WORDS = 0.700


def detect_pauses(filename):
    audio_data, sample_rate = librosa.load(filename)

    # Split audio data into chunks of 10 ms
    # Size of chunks in samples
    chunk_size = int(sample_rate / 100)
    chunks = np.split(audio_data, np.arange(chunk_size, len(audio_data), chunk_size))

    # Calculate the amplitude of each chunk
    amplitudes = [np.linalg.norm(chunk, ord=2) for chunk in chunks]

    # Define a threshold for silence
    threshold = 0.1

    # Detect silence
    silences = [amplitude < threshold for amplitude in amplitudes]

    # Print the result
    for i, is_silence in enumerate(silences):
        print(f'Chunk {i}: {"Silence" if is_silence else "Sound"}')


def decode_sound(sound):
    filename = 'sound.wav'
    sample_rate, audio_data = wav.read(filename)

    # Calculate duration
    duration = len(audio_data) / sample_rate
    print(f'Duration: {duration} seconds')

    # FFT
    fft_result = np.fft.rfft(audio_data)
    frequencies = np.fft.rfftfreq(audio_data.size, 1 / sample_rate)

    # Get the frequency of the maximum absolute value in the FFT result
    estimated_frequency = frequencies[np.argmax(np.abs(fft_result))]

    print(f'Estimated Frequency: {estimated_frequency} Hz')


def play_sound(frequency, duration_milliseconds):
    # Convert duration to seconds
    duration_seconds = duration_milliseconds / 1000.0

    # Choose a sample rate (how many measurements per second)
    sample_rate = 44100

    # Generate the time values for one cycle of the sine wave
    t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds), False)

    # Generate a sine wave of the desired frequency at these time values
    note = np.sin(frequency * t * 2 * np.pi)

    # Ensure that the highest value is in the 16-bit range
    audio = note * (2 ** 15 - 1) / np.max(np.abs(note))

    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Write the audio data to a .wav file
    write("sound.wav", sample_rate, audio)

    # Load the audio file into a pydub.AudioSegment
    sound = AudioSegment.from_wav("sound.wav")

    # Play the audio file
    play(sound)


def play_morse_code(morse_code):
    for letter in morse_code:
        for dot_dash in letter:
            match dot_dash:
                case '.':
                    play_sound(*DOTS)
                    sleep(PAUSE_BETWEEN_DASH_DOT)
                case '-':
                    play_sound(*DASHES)
                    sleep(PAUSE_BETWEEN_DASH_DOT)
                case ' ':
                    sleep(PAUSE_BETWEEN_WORDS)
                case _:
                    raise ValueError(f'Invalid character {letter} in morse code')


def encode_morse_code(message):
    morse_code = []
    for word in message.upper().split():
        for letter in word:
            morse_code.append(INTERNATIONAL_MORSE_CODE[letter])
        morse_code.append(' ')
    return morse_code


if __name__ == '__main__':
    while True:
        message = input('What message would you like to encode? ')
        morse_code = encode_morse_code(message)
        print(morse_code)
        play_morse_code(morse_code)
        decode_sound('sound.wav')
        detect_pauses('sound.wav')

