import numpy as np
import soundfile as sf
from constants import (const,
                       DOTS,
                       DASHES,
                       SAMPLE_RATE,
                       INTERNATIONAL_MORSE_CODE,
                       MAX_CODE_LENGTH,
                       PAUSE_BETWEEN_DASH_DOT,
                       PAUSE_BETWEEN_LETTERS,
                       PAUSE_BETWEEN_WORDS)

from decode_morse_code_sound_file import decode_morse_code_sound_file


def generate_sound(frequency, duration, sample_rate=SAMPLE_RATE):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    if frequency == 0:
        signal = np.zeros_like(t)
    else:
        # generate sinusoidal audio signal
        signal = np.sin(2 * np.pi * frequency * t)
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


def pretty_print(legend):
    str_letters = ''
    str_codes = ''
    letter_spaces = (MAX_CODE_LENGTH - 1) * ' '
    for letter, morse_code in legend:
        str_letters += letter + letter_spaces
        str_codes += morse_code.ljust(MAX_CODE_LENGTH, ' ')

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
        decoded = decode_morse_code_sound_file()
        pretty_print(decoded)
