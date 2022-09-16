# libraries
from math import *
from random import *
from constants import *

"""
This function calculates the poisson distribution based on
m average number of events and x number of successes
"""
def poissonDistribution():
    
	m = randint(PROBABILITY_MIN, PROBABILITY_MAX)
	x = randint(PROBABILITY_MIN, PROBABILITY_MAX)
    
	probability = ((pow(m, x) * exp(-m)) / factorial(x)) * 100

	return probability

"""
This function returns an specific operation based on the poisson
probability
"""
def getInstruction(probability):

	if(probability >= 0 and probability < CALC_PROBABILITY):
    	
		return OPERATIONS[0]

	elif(probability >= CALC_PROBABILITY and probability < READ_PROBABILITY):
    	
		return OPERATIONS[1]

	else:
    	
		return OPERATIONS[2]

"""
This function returns an specific memory direction based on the
poisson probability
"""
def getMemoryDirection(probability):

	# memory direction 0000
	if(probability >= 0 and probability < MEMORY_BLOCKS_PROB[0]):
    	
		return MEMORY_BLOCKS_DIR[0]

	# memory direction 0001
	elif(probability >= MEMORY_BLOCKS_PROB[0] and probability < MEMORY_BLOCKS_PROB[1]):
    	
		return MEMORY_BLOCKS_DIR[1]

	# memory direction 0010
	elif(probability >= MEMORY_BLOCKS_PROB[1] and probability < MEMORY_BLOCKS_PROB[2]):
    	
		return MEMORY_BLOCKS_DIR[2]

	# memory direction 0011
	elif(probability >= MEMORY_BLOCKS_PROB[2] and probability < MEMORY_BLOCKS_PROB[3]):
    	
		return MEMORY_BLOCKS_DIR[3]

	# memory direction 0100
	elif(probability >= MEMORY_BLOCKS_PROB[3] and probability < MEMORY_BLOCKS_PROB[4]):
    	
		return MEMORY_BLOCKS_DIR[4]

	# memory direction 0101
	elif(probability >= MEMORY_BLOCKS_PROB[4] and probability < MEMORY_BLOCKS_PROB[5]):
    	
		return MEMORY_BLOCKS_DIR[5]

	# memory direction 0110
	elif(probability >= MEMORY_BLOCKS_PROB[5] and probability < MEMORY_BLOCKS_PROB[6]):
    	
		return MEMORY_BLOCKS_DIR[6]

	# memory direction 0111
	else:
    	
		return MEMORY_BLOCKS_DIR[7]

"""
This function generates a random hex number of 4 bits
"""
def getValue():
    
    return hex(randint(0, VALUE_MAX))













"""
for i in range(0,5):
    
	probability = poissonDistribution()

	print(getInstruction(probability))

print()

for i in range(0,5):
    
	probability = poissonDistribution()

	print(getMemoryDirection(probability))

print()

print(hex(65535))
"""
