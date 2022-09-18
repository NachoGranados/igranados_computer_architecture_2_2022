# libraries
from math import *
from random import *
from constants import *
from models import *

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
distribution
"""
def getOperation(probability):

	if(probability >= 0 and probability < CALC_PROBABILITY):

		return OPERATIONS[0]

	elif(probability >= CALC_PROBABILITY and probability < READ_PROBABILITY):

		return OPERATIONS[1]

	else:

		return OPERATIONS[2]

"""
This function returns an specific memory direction based on the
poisson distribution
"""
def getMemoryDirection(probability):

	# memory direction 0000
	if(probability >= 0 and probability < MEMORY_BLOCKS_PROB[0]):

		return MEMORY_BLOCKS_DIR[0]

	# memory direction 0001
	elif(probability >= MEMORY_BLOCKS_PROB[0] and
	     probability < MEMORY_BLOCKS_PROB[1]):

		return MEMORY_BLOCKS_DIR[1]

	# memory direction 0010
	elif(probability >= MEMORY_BLOCKS_PROB[1] and
	     probability < MEMORY_BLOCKS_PROB[2]):

		return MEMORY_BLOCKS_DIR[2]

	# memory direction 0011
	elif(probability >= MEMORY_BLOCKS_PROB[2] and
	     probability < MEMORY_BLOCKS_PROB[3]):

		return MEMORY_BLOCKS_DIR[3]

	# memory direction 0100
	elif(probability >= MEMORY_BLOCKS_PROB[3] and
	     probability < MEMORY_BLOCKS_PROB[4]):

		return MEMORY_BLOCKS_DIR[4]

	# memory direction 0101
	elif(probability >= MEMORY_BLOCKS_PROB[4] and
	     probability < MEMORY_BLOCKS_PROB[5]):

		return MEMORY_BLOCKS_DIR[5]

	# memory direction 0110
	elif(probability >= MEMORY_BLOCKS_PROB[5] and
	     probability < MEMORY_BLOCKS_PROB[6]):

		return MEMORY_BLOCKS_DIR[6]

	# memory direction 0111
	else:

		return MEMORY_BLOCKS_DIR[7]

"""
This function generates a hex number of 4 bits based on poisson
distribution
"""
def getValue():
    
	probability = trunc(poissonDistribution() * 10000)

	while(probability > VALUE_MAX):
    
		probability = trunc(poissonDistribution() * 10000)

	return hex(probability)

"""
This function generates a new instruction for the received CPU
"""
def generateInstruction(cpu):        
        
	cpuNumber = cpu.getNumber()

	operation = getOperation(poissonDistribution())

	instruction = Instruction(cpuNumber, operation)

	# not calc operation
	if(operation != OPERATIONS[0]):
		
		memoryDirection = getMemoryDirection(poissonDistribution())

		instruction.setMemoryDirection(memoryDirection)

		# write operation
		if(operation == OPERATIONS[2]):
		
			value = getValue()

			instruction.setValue(value)

	return instruction

"""
This function indicates to the CPU to generate a new instruction
"""
def threadFunction(cpu):
    
	instruction = generateInstruction(cpu)

	cpu.setCurrentInstruction(instruction)
	
	#print("CPUNumber = ", instruction.getCpuNumber())
	#print("Operation = ", instruction.getOperation())
	#print("MemoryDirection = ", instruction.getMemoryDirection())
	#print("Value = ", instruction.getValue())
    
	#return instruction

"""
This function assign the respective four block of cache memory to the received CPU

def assignCacheBlocks(cpu):

	for i in range(0, 4):
    
		memoryIndex = randint(0, 7)

		cacheBlock = CacheBlock(i, INITIAL_CACHE_STATE, MEMORY_BLOCKS_DIR[memoryIndex], 0)

		cpu.cache.blocks.append(cacheBlock)
		
		memoryIndex = randint(0, 7)

		cpu.cache.block1 = CacheBlock(1, INITIAL_CACHE_STATE, MEMORY_BLOCKS_DIR[memoryIndex], 0)

		memoryIndex = randint(0, 7)

		cpu.cache.block2 = CacheBlock(2, INITIAL_CACHE_STATE, MEMORY_BLOCKS_DIR[memoryIndex], 0)

		memoryIndex = randint(0, 7)

		cpu.cache.block3 = CacheBlock(3, INITIAL_CACHE_STATE, MEMORY_BLOCKS_DIR[memoryIndex], 0)
"""

"""
This function assign the cache and controller to the received CPU
"""
def assignResources(cpuArray):
    
	for cpu in cpuArray:

		# create cache
		cache = Cache(cpu.getNumber())

		# assign cache blocks to the CPU cache
		for i in range(0, 4):
        
			memoryIndex = randint(0, 7)

			cacheBlock = CacheBlock(i, INITIAL_CACHE_STATE, MEMORY_BLOCKS_DIR[memoryIndex], 0)

			cache.blocks.append(cacheBlock)

		# assign cache to CPU
		cpu.setCache(cache)

		# create controller
		controller = Controller(cpu.getNumber())

		# assign controller to CPU
		cpu.setController(controller)

"""
This function creates the main memory dictionary
"""
def startMemory():
        
        dictionary = {}

        for i in MEMORY_BLOCKS_DIR:

            dictionary[i] = hex(0)

        return dictionary






























"""
"""
def executeInstruction(cpu):
	pass





























