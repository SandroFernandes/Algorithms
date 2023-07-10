import sys
import numpy as np
import soundfile as sf
from constants import (const,
                       MORSE_CODE_DICT,
                       END_OF_DOT_DASH_DIFF,
                       END_OF_LETTER_DIFF)


def decode_morse_code_sound_file(sound_file='sound.wav'):
    # Load the audio file
    audio, _ = sf.read(sound_file)

    # find silence
    silence = np.where(audio == 0)[0]
    silence_diff = np.diff(silence)

    change_indices = np.where(silence_diff[:-1] != silence_diff[1:])[0] + 1

    # add 0 first indexes
    change_indices = np.insert(change_indices, 0, 0)
    differences = np.diff(change_indices)
    # get the smallest difference, that is the dot
    dot_dif = np.min(differences)
    # dash is 3 times the dot
    dash_dif = 3 * dot_dif
    # append an end of dash or dot
    differences = np.append(differences, END_OF_DOT_DASH_DIFF)
    # append an end of letter
    differences = np.append(differences, END_OF_LETTER_DIFF)

    code = ''
    letter_code = []
    for i in range(len(differences)):
        if differences[i] == 0:
            continue
        # dot
        if differences[i] == dot_dif:
            code += const.DOT
        # dash
        elif differences[i] == dash_dif:
            code += const.DASH
        # end of dot or dash
        elif differences[i] == END_OF_DOT_DASH_DIFF:
            pass
        # end of a letter
        elif differences[i] == END_OF_LETTER_DIFF:
            letter_code.append((MORSE_CODE_DICT[code], code))
            code = ''
        else:
            # end of a word
            letter_code.append((MORSE_CODE_DICT[code], code))
            letter_code.append((' ', ' '))
            code = ''

    return letter_code


if __name__ == '__main__':
    # parse filename from command line
    args = sys.argv[1:]
    if len(args) == 1:
        sound_file_name = args[0]
    else:
        sound_file_name = 'A_through_Z_in_Morse_code.wav'

    print(decode_morse_code_sound_file(sound_file_name))
