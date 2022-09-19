# libraries
from math import *
from random import *
from constants import *
from threading import *

class MainMemory:
    
    def __init__(self):        
        self.dictionary = {}

        self.startMemory()

    def getDictionary(self):
        return self.dictionary

    def setDictionary(self, dictionary):
        self.dictionary = dictionary

    """
    This function creates the main memory dictionary
    """
    def startMemory(self):        
        
        #dictionary = {}

        for i in MEMORY_BLOCKS_DIR:

            self.dictionary[i] = hex(0)

        #return dictionary

class Bus:
    
    def __init__(self, cpuArray, mainMemory):
        self.cpuArray = cpuArray
        self.mainMemory = mainMemory
        self.lock = Lock()
    
    def getCpuArray(self):
        return self.cpuArray

    def setCpuArray(self, cpuArray):
        self.cpuArray = cpuArray

    def getMainMemory(self):
        return self.mainMemory

    def setMainMemory(self, mainMemory):
        self.mainMemory = mainMemory

    def getLock(self):
        return self.lock

    def setLock(self, lock):
        self.lock = lock

class Instruction:
    
    #def __init__(self, cpuNumber, operation):
    def __init__(self, operation):        
        #self.cpuNumber = cpuNumber
        self.operation = operation
        self.memoryDirection = None
        self.value = None

    """
    def getCpuNumber(self):
        return self.cpuNumber

    def setCpuNumber(self, cpuNumber):
        self.cpuNumber = cpuNumber
    """

    def getOperation(self):
        return self.operation

    def setOperation(self, operation):
        self.operation = operation

    def getMemoryDirection(self):
        return self.memoryDirection

    def setMemoryDirection(self, memoryDirection):
        self.memoryDirection = memoryDirection

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

class Cache:
    
    #def __init__(self, cpuNumber):
    def __init__(self):
        #self.cpuNumber = cpuNumber # unnecessary
        self.blocks = []

        #self.hitAlert = 0
        #self.missAlert = 0
    
    """
    def getCpuNumber(self):
        return self.cpuNumber

    def setCpuNumber(self, cpuNumber):
        self.cpuNumber = cpuNumber
    """

    def getBlocks(self):
        return self.blocks

    def setBlocks(self, blocks):
        self.blocks = blocks

    """
    def getHitAlert(self):
        return self.hitAlert

    def setHitAlert(self, hitAlert):
        self.hitAlert = hitAlert

    def getMissAlert(self):
        return self.missAlert

    def setMissAlert(self, missAlert):
        self.missAlert = missAlert
    """

class CacheBlock:
    
    def __init__(self, number, state, memoryDirection, value):
        self.number = number
        self.state = state
        self.memoryDirection = memoryDirection
        self.value = value

    def getNumber(self):
        return self.number

    def setNumber(self, number):
        self.number = number

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def getMemoryDirection(self):
        return self.memoryDirection

    def setMemoryDirection(self, memoryDirection):
        self.memoryDirection = memoryDirection

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

class Controller:
    
    #def __init__(self, cpuNumber, cache):
    def __init__(self):
        #self.cpuNumber = cpuNumber # unnecessary
        self.cache = None
        self.hitAlert = 0
        self.missAlert = 0
    
    """
    def getCpuNumber(self):
        return self.cpuNumber

    def setCpuNumber(self, cpuNumber):
        self.cpuNumber = cpuNumber
    """

    def getCache(self):
        return self.cache

    def setCache(self, cache):
        self.cache = cache

    def getHitAlert(self):
        return self.hitAlert

    def setHitAlert(self, hitAlert):
        self.hitAlert = hitAlert

    def getMissAlert(self):
        return self.missAlert

    def setMissAlert(self, missAlert):
        self.missAlert = missAlert

    def localSearch(self):
        pass

    def remoteSearch(self):
        pass

    def invalidateCaches(self):
        pass

class CPU:
    
    def __init__(self, number):        
        self.number = number        
        self.currentInstruction = None
        self.controller = None

        self.assignResources()

        #self.cache = None

    def getNumber(self):
        return self.number

    def setNumber(self, number):
        self.number = number

    """
    def getCache(self):
        return self.cache

    def setCache(self, cache):
        self.cache = cache
    """

    def getCurrentInstruction(self):
        return self.currentInstruction

    def setCurrentInstruction(self, currentInstruction):
        self.currentInstruction = currentInstruction

    def getController(self):
        return self.controller

    def setController(self, controller):
        self.controller = controller

    """
    This function calculates the poisson distribution based on
    m average number of events and x number of successes
    """
    def poissonDistribution(self):
        
        m = randint(PROBABILITY_MIN, PROBABILITY_MAX)
        x = randint(PROBABILITY_MIN, PROBABILITY_MAX)
        
        probability = ((pow(m, x) * exp(-m)) / factorial(x)) * 100

        return probability

    """
    This function returns an specific operation based on the poisson
    distribution
    """
    def getOperation(self, probability):

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
    def getMemoryDirection(self, probability):

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
    def getValue(self):
        
        probability = trunc(self.poissonDistribution() * 10000)

        while(probability > VALUE_MAX):
        
            probability = trunc(self.poissonDistribution() * 10000)

        return hex(probability)

    """
    This function generates a new instruction for the received CPU
    """
    def generateInstruction(self):        
            
        #cpuNumber = cpu.getNumber()

        operation = self.getOperation(self.poissonDistribution())

        instruction = Instruction(operation)

        # not calc operation
        if(operation != OPERATIONS[0]):
            
            memoryDirection = self.getMemoryDirection(self.poissonDistribution())

            instruction.setMemoryDirection(memoryDirection)

            # write operation
            if(operation == OPERATIONS[2]):
            
                value = self.getValue()

                instruction.setValue(value)

        #return instruction

        self.currentInstruction = instruction

    """
    This function indicates to the CPU to generate a new instruction
    
    def threadFunction(self, cpu):
        
        instruction = generateInstruction(cpu)

        cpu.setCurrentInstruction(instruction)
    """

    """
    This function assign controller and cache to the CPU
    """
    def assignResources(self):
        
        #for cpu in cpuArray:

        # create controller
        controller = Controller()

        # create cache
        #cache = Cache(cpu.getNumber())
        cache = Cache()

        # assign cache blocks to the cache **************************************************************** NO SE SABE SI ES ASI
        for i in range(0, 4):
        
            memoryIndex = randint(0, 7)

            cacheBlock = CacheBlock(i, INITIAL_CACHE_STATE, MEMORY_BLOCKS_DIR[memoryIndex], 0)

            cache.blocks.append(cacheBlock)

        # assign cache to controller
        controller.setCache(cache)

        # create controller
        #controller = Controller(cpu.getNumber())

        # assign controller to CPU
        #cpu.setController(controller)
        self.controller = controller

    def executeInstruction(self):
        pass