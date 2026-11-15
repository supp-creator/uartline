# ===================================================
# pcm.py
# Author/s: Tyrone Sarmiento
# Date of Last Edit: 15-11-2026
# ==================================================
# PURPOSE
#   The PCM process (sample, quantize, encode). And the inverse process at receiver.
#   Quantize and dequantize must use the same rules.
#
# RECOMMENDED LIBRARIES
#   numpy alone should be enough.
#
# STANDARDS
#   n = 8, range [-1, 1), step = 2 / 2**n = 1/128
#   level l = clip(round(x / step) + 2**(n-1), 0, 2**n - 1)
#   amplitude A = (l - 2**(n-1)) * step
#   Level 128 is exactly 0 amplitude.
#
# CONTENTS
#   flat_top_sample(x, fs_in, fs_out) -> samples_at_fs_out
#       IN: array of floats at fs_in (fs_in higher than fs_out ideally)
#       OUT: array of floats at fs_out
#
#   quantize(x, n_bits) -> levels
#       IN: float array [-1, 1). Values out of range clipped.
#       OUT: uint8 array (for n_bits <= 8)
#
#   dequantize(levels, n_bits)
#       IN: uint8 array
#       OUT: float array in [-1, 1). Exact inverse of quantize().
#
#   sqnr_db(x) -> float 
#       6.02n + 1.76 dB 
#
# NOTES
#   * n_bits is a parameter sweep for later.
# =================================================

def flat_top_sample(x, fs_in, fs_out) :
    #to-do
    pass

def quantize(x, n_bits) :
    #to -do 
    pass

def dequantize(levels, n_bits) :
    #to-do
    pass

def sqnr_db(x) -> float:
    return 6.02*x + 1.76
