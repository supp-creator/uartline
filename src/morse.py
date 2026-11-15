# ==================================================
# morse.py
# Author/s: Tyrone Sarmiento
# Date of Last Edit:15-11-2026
# ==================================================
# PURPOSE
#   Turn text into a keyed 700 Hz tone. Turn recovered signal back into text.
#
# RECOMMENDED LIBRARIES
#   numpy should be enough.
#
# CONTENTS
#   MORSE_TABLE : dict mapping characters to dot/dash strings e.g. "...---..."
#
#   text_to_keying(text, fs, wpm=30) -> onoff array
#       IN: text (str), wpm (int or float), fs in Hz
#       OUT: array of bools.
#
#   generate_tone(text, wpm, fs, tone_hz=700) -> samples
#       IN: text (str), wpm (int or float), fs in Hz, tone_hz 
#       OUT: float array in [-1,1): sine at tone_hz multiplied by keying.
#
#   onoff_to_text(onoff array, fs) -> str 
#       IN: bool array from text_to_keying 
#       OUT: decoded text 
#
# NOTES
#   * dot = 1.2/(wpm) seconds; dash = 3 dots; gap between letter = 1 dot; 
#       gap between words = 7 dots.
#   * 30 wpm is max. Use something else for testing
# ==================================================

MORSE_TABLE = {
        # Convert each letter to capital first. Call .upper()
        # Morse has no distinction between cases.
        'A' : ".-",
        'B' : "-...",
        'C' : "-.-.",
        'D' : "-..",
        'E' : ".",
        'F' : "..-.",
        'G' : "--.",
        'H' : "....",
        'I' : "..",
        'J' : ".---",
        'K' : "-.-",
        'L' : ".-..",
        'M' : "--",
        'N' : "-.",
        'O' : "---",
        'P' : ".--.",
        'Q' : "--.-",
        'R' : ".-.",
        'S' : "...",
        'T' : "-",
        'U' : "..-",
        'V' : "...-",
        'W' : ".--",
        'X' : "-..-",
        'Y' : "-.--",
        'Z' : "--..",
        '0' : "-----",
        '1' : ".----",
        '2' : "..---",
        '3' : "...--",
        '4' : "....-",
        '5' : ".....",
        '6' : "-....",
        '7' : "--...",
        '8' : "---..",
        '9' : "----."
        # Space is a time poause. Check notes.
        }

def text_to_keying(text, fs, wpm=30) :
    #to -do 
    pass

def generate_tone(text, fs, wpm=30, tone_hz=700) :
    # to - do
    pass

def onoff_to_text(onoff, fs) -> str:
    #to-do
    pass
