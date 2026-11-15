# ===================================================
# link.py
# Author/s:
# Date of Last Edit:
# ===================================================
# PURPOSE
#   This is the only part of the program that talks with the serial port.
#   It sends the stream, reads it back in the TXD-RXD loop, applies the jitter,
#   and timestampes every read and write.
#
# RECOMMENDED LIBRARIES
#   pyserial
#   threading, queue     : bro, we'll need to send & receive simultaneously.
#   time                 : perf_counter() for ALL timestamps. One clock for all.
#   numpy                : np.random.default_rng(seed) for reproducible jitter
#
# CONTENTS
#   open_port(port, baud, timeout)
#       IN: port name ('/dev/ttyUSB0' on Linux, 'COM3' on Windows), baud,
#           read timeout in seconds.
#       OUT: opened port, 8 data bits, no parity, 1 stop bit 
#
#   apply_jitter(max_ms, rng)
#       IN: maximum delay in ms, numpy random number generator
#       OUT: nothing returned. delay applied in stream. Apply once per block
#            before stream.
#
#   transmit(stream, serial, block_bytes, jitter_max, rng)
#       IN: uint8 stream, open port, bytes per block (66), max jitter, rng 
#       OUT: list of (timestamp, first_byte_index) recorded BEFORE each write.
#
#   receive(serial, expected_bytes, timeout) -> (rx_bytes, rx_log)
#       IN: open port, number of bytes expected, overall timeout 
#       OUT: uint8 array of whatever that arrived, list of (timestamps, bytes_read_so_far)
#       
#   loopback(stream, port, baud, jitter_max, seed)
#       Starts the receive thread FIRST, then transmits, then joins data within time.
#
# NOTES
#   * receive() should run as its own thread. Read and stamp, that's it.
#   * 8N1 framing.
# ==================================================

def open_port(port, baud, timeout) :
    # to -do
    pass

def apply_jitter(max_ms, rng) :
    # to - do 
    pass

def transmit(stream, serial, block_bytes, jitter_max, rng) :
    #to - do
    pass

def receive(serial, expected_bytes, timeout) :
    # to -do 
    pass

def loopback(stream, port, baud, jitter_max, seed) :
    # to - do
    pass
