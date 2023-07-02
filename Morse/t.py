import numpy as np
import librosa

# Morse Code Dictionary
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B',
    '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K',
    '.-..': 'L', '--': 'M', '-.': 'N',
    '---': 'O', '.--.': 'P', '--.-': 'Q',
    '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W',
    '-..-': 'X', '-.--': 'Y', '--..': 'Z'
}

# Constants
DOT_DURATION = 0.1  # The duration of a "dot" in seconds
DASH_DURATION = 0.3  # The duration of a "dash" in seconds
LETTER_GAP = 0.3  # The duration of the gap between letters in a word
WORD_GAP = 0.7  # The duration of the gap between words

# Load the audio file
audio, sample_rate = librosa.load('sound.wav')

# Chunk the audio into frames of 10 ms each
frame_length = int(sample_rate * 0.01)  # 10 ms frame
audio_frames = librosa.util.frame(audio, frame_length=frame_length, hop_length=frame_length)

# Calculate the average absolute amplitude of each frame
average_amplitudes = np.mean(np.abs(audio_frames), axis=0)

# Threshold average amplitude to distinguish signal from silence
silence_threshold = np.median(average_amplitudes) / 2
is_signal = average_amplitudes > silence_threshold

# Convert signal to Morse code
morse_code = ''
current_symbol = ''
for i, this_frame_is_signal in enumerate(is_signal):
    if this_frame_is_signal:
        if current_symbol and current_symbol[-1] == ' ':
            # If the silence was short, it's an intra-character gap; otherwise, it's a space.
            silence_duration = i * 0.01 - len(current_symbol) * 0.01
            if silence_duration >= WORD_GAP:
                morse_code += ' '
            # Convert current Morse code symbol to letter
            morse_code += MORSE_CODE_DICT.get(current_symbol.strip(), '?')
            current_symbol = ''
        # If the tone is short, it's a dot; if it's long, it's a dash.
        tone_duration = np.sum(is_signal[max(0, i-10):i]) * 0.01  # Check tone duration for last 10 frames
        if tone_duration < DOT_DURATION + DASH_DURATION / 2:
            current_symbol += '.'
        else:
            current_symbol += '-'
    else:
        current_symbol += ' '

# Convert the last symbol if it hasn't been converted yet
if current_symbol.strip():
    morse_code += MORSE_CODE_DICT.get(current_symbol.strip())
