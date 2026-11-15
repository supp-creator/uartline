# =================================================
# metrics.py
# Author/s:
# Date of Last Edit:
# =================================================
# PURPOSE
#   Compute every number outputted by program and every theoretical value.
#   Compares them against each other.
#
# RECOMMENDED LIBRARIES
#   numpy
#
# METRICS TO MEASURE
#   ber(tx_bytes, rx_bytes, valid_mask=None) -> float
#       IN: uint8 arrays of equal length
#       OUT: bit errors / total bits
#       
#   byte_loss_rate(report, n_sent) -> float 
#       from framing.realign()
#
#   latency(tx_log, rx_log) -> dict
#       IN: logs from link.py
#       OUT: {'mean_ms', 'p95_ms', 'max_ms', 'jitter_ms'} PER BYTE...Or per block.
#
#   throughput(rx_log) -> float
#       bytes per second successfully delivered.
#
#   char_error_rate(text_tx, text_rx) -> float 
#       OUT: incorrect characters / total characters 
#   
# THEORY
#   payload_rate(baud) -> baud * 8 / 10         (8N1 framing)
#   required_rate(fs, n_bits, block_size, overhead_bytes=2) -> bits/s 
#   breakpoint_baud(fs,n_bits, block_size) -> required_rate * 10 / 8 
#   sqnr_theory(n_bits) -> 6.02*n + 1.76 
#
# NOTES
#   * Stopping criteria for BER: >= 100 errors or >= 1,000,000 bits
# =================================================

def ber (tx_bytes, rx_bytes, valid_mask=None) -> float :
    # to-do 
    pass

def byte_loss_rate(report, n_sent) -> float :
    # to - do 
    pass

def latency(tx_log, rx_log) :
    #to-do 
    pass 

def throughput(rx_log) -> float :
    #to-do 
    pass 

def char_error_rate(text_tx, text_rx) -> float :
    #to-do 
    pass
    
