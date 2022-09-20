PROBABILITY_MIN = 1
PROBABILITY_MAX = 14

VALUE_MAX = 65535

CALC_PROBABILITY = 20/3
READ_PROBABILITY = 40/3

OPERATIONS = ["CALC", "READ", "WRITE"]

CALC_INDEX = 0
READ_INDEX = 1
WRITE_INDEX = 2


MEMORY_BLOCKS_DIR = [bin(0), bin(1), bin(2), bin(3),
                     bin(4), bin(5), bin(6), bin(7)]

MEMORY_BLOCKS_PROB = [5/2,  5,  15/2, 10,
                      25/2, 15, 35/2]

INITIAL_CACHE_STATE = "I"
INITIAL_CACHE_VALUE = "0x" + "{0:016x}".format(0)

INITIAL_MAIN_MEMORY_VALUE = "0x" + "{0:016x}".format(0)

MODIFIED = "M"
EXCLUSIVE = "E"
SHARED = "S"
INVALID = "I"

HIT = 1
MISS = 0

SETS = 4

TIMER = 3