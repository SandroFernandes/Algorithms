import types

const = types.SimpleNamespace()
const.DOT = '.'
const.DASH = '_'
const.SPACE = ' '

# Morse Code Entry by letter
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

MAX_CODE_LENGTH = max([len(code) for code in MORSE_CODE_DICT.keys()]) + 1

# Frequency in Hz of the sound, duration in seconds
FREQUENCY = 700
DOTS = (FREQUENCY, 0.100)
DASHES = (FREQUENCY, 0.300)

PAUSE_BETWEEN_DASH_DOT = (0, 0.100)
PAUSE_BETWEEN_LETTERS = (0, 0.300)
PAUSE_BETWEEN_WORDS = (0, 0.700)

SAMPLE_RATE = 44100

# For a 700 Hz sound
# 700 Hz * 0.100 s = 70 ?????
DOT_DIFF = int(DOTS[0] * DOTS[1])
# 700 Hz * 0.300 s = 210 ?????
DASH_DIFF = int(DASHES[0] * DASHES[1])
# 44100 * 0.100 = 4410
END_OF_DOT_DASH_DIFF = int(PAUSE_BETWEEN_DASH_DOT[1] * SAMPLE_RATE)
# 44100 * 0.300 = 13230 + 4410 = 17640
END_OF_LETTER_DIFF = int(PAUSE_BETWEEN_LETTERS[1] * SAMPLE_RATE) + END_OF_DOT_DASH_DIFF
