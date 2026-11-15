# ===================================================================
# detector.py
# Author/s: Tyrone Sarmiento
# Date of Last Edit: 15-11-2026
# ===================================================================
# PURPOSE
#   Converts the dequantized samples back to Morse beeps or silence.
#   All filters should be digital and sequential. Oof.
#
# RECOMMENDED LIBRARIES
#   scipy.signal
#   numpy
#
# CONTENTS
#   bandpass(x, fs, low, high, order)
#       IN: array of floats; edge of band in Hz; order 
#       OUT: also an array of floats, same length. Rejects noise
#
#   quadrature_mix(x, fs, fc = 700) -> (i, q)
#       IN: array of floats;
#       OUT: (x*cos(2*pi*fc*n/fs), x*sin(2*pi*fc*n/fs)), n =sample index
#
#   lowpass(fs, cutoff = 50Hz, order)
#       IN: array of floats; Apply to both i & q.
#       OUT: Removes 2*fc (1400Hz) mixing product.
#
#   envelope(i, q)
#       sqrt(i**2 + q**2). Must come after lowpass.
#
#   apply_threshold(frac=0.5, floor=10, peak=95)
#       IN: envelope
#       OUT: array of booleans. threshold = floot + frac * (peak - floor)
#
#  NOTES
#   * samples -> bandpass -> mix with cos/sin at fc -> lowpass (I and Q) 
#       -> envelope -> threshold
#   * Values for apply_threshold are tentative and can change.
# =====================================================================

import numpy as np

def bandpass(x, fs, low, high, order) :
    #to-do
    pass

def quadrature_mix(x, fs, fc = 700, n=0):
    x = np.asarray(x)

    n = np.arange(n, n + len(x))

    phase = 2 * np.pi * fc * n / fs

    i = x * np.cos(phase)
    q = -x * np.sin(phase)

    return (i, q)

def lowpass(fs, order, cutoff = 50):
    # to - do
    pass

def envelope(i, q):
    return np.sqrt(i**2 + q**2)

def apply_threshold(frac=0.5, floor=10, peak=95) :
    # to -do 
    pass
