from re import M
from tkinter import E


PROBABILITY_MIN = 1
PROBABILITY_MAX = 14

VALUE_MAX = 65535

CALC_PROBABILITY = 20/3
READ_PROBABILITY = 40/3

OPERATIONS = ["CALC", "READ", "WRITE"]

CALC_INDEX = 0
READ_INDEX = 1
WRITE_INDEX = 2


MEMORY_BLOCKS_DIR = ["0b0000", "0b0001", "0b0010", "0b0011",
                     "0b0100", "0b0101", "0b0110", "0b0111"]

MEMORY_BLOCKS_PROB = [5/2,  5,  15/2, 10,
                      25/2, 15, 35/2]

INITIAL_CACHE_STATE = "I"
INITIAL_CACHE_VALUE = 0

MODIFIED = "M"
EXCLUSIVE = "E"
SHARED = "S"
INVALID = "I"
