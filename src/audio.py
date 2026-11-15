# ====================================================
# audio.py 
# Author/s :
# Date of Last Edit:
# ====================================================
# PURPOSE
#   Connects to laptop sound card. Gets audio in and returns an array of floats.
#
# RECOMMENDED LIBRARIES
#   pyaudio         : for live capture and playback
#   scipy           : scipy.signal for anti-alias filter and rate conversion.
#                     scipy.io.wavfile for reading/writing WAV files.
#   numpy
#
# EXPECTED FUNCTIONS
#   record(duration)
#       IN: duration in seconds
#       OUT: float array [-1, 1] (convert from int16)
#
#   resample_to_fs(x, capture_rate, fs)
#       IN: float array from record()
#       OUT: float array at sampling rate (fs).
#
# 
# NOTES
#   * Record to a WAV for lossless audio.
#   * Use scipy.signal.resample_poly in resample_to_fs()
#   * Different devices' audio cards captures audio at different 
#     rates.
# ====================================================

def record(duration) :
    #to-do 
    pass

def resample_to_fs(x, capture_rate, fs) :
    #to-do 
    pass

