# ===================================================
# framing.py
# Author/s: Tyrone Sarmiento
# Date of Last Edit: 15-11-2026
# ===================================================
# PURPOSE
#   Add a sync byte and a sequence number to each block of samples. So 
#   the receiver can restore block positions after UART link.
#
# RECOMMENDED LIBRARIES
#   numpy should be good enough.
#
# CONTENTS
#   build_stream(data, block_size=64)
#       IN: array of uint8 quantized levels; size of block
#       OUT: array of uint8 with headers. Pad the last block with level 128
#           if payload is not a multiple of block size(64). Record actual length.
#
#   realign(rx_bytes, blocks_sent, block_size=64) -> (data, report)
#       IN: array of uint8 as read from port; block size; number of blocks sent 
#       OUT: payload is an array of uint8 of blocks sent * block size, lost
#           blocks should be filled with level 128 (zero amplitude).
#           report = dict: lost_blocks, lost_bytes, duplicate_blocks,
#                         corrupted headers
#
# NOTES
#   * The block format is 1 sync byte + 1 sequence byte + 64 data bytes
#   * So 66 bytes per block.
# ====================================================

def build_stream(data, block_size=64) :
    #to - do
    pass

def realign(rx_bytes, block_sent, block_size=64):
    #to -do 
    pass
