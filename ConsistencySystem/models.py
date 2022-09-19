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
        
        for i in MEMORY_BLOCKS_DIR:

            self.dictionary[i] = hex(0)

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

    def acquireLock(self):
        self.lock.acquire()

    def releaseLock(self):
        self.lock.release()

class Instruction:
    
    def __init__(self, cpuNumber, operation):
        self.cpuNumber = cpuNumber
        self.operation = operation
        self.memoryDirection = None
        self.value = None

    def getCpuNumber(self):
        return self.cpuNumber

    def setCpuNumber(self, cpuNumber):
        self.cpuNumber = cpuNumber

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
    
    def __init__(self):
        self.blocks = []

    def getBlocks(self):
        return self.blocks

    def setBlocks(self, blocks):
        self.blocks = blocks

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
    
    def __init__(self):
        self.cache = None
        self.hitAlert = 0
        self.missAlert = 0
    
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

    def resetAlerts(self):
        self.hitAlert = 0
        self.missAlert = 0

    """
    This function checks if the cache has the requested block to read it
    """
    def localRead(self, instruction):

        memoryDirection = instruction.getMemoryDirection()

        blocks = self.cache.blocks

        for block in blocks:

            # memory direction match
            if(block.getMemoryDirection() == memoryDirection):

                state = block.getState()

                # state M, E or S
                if(state == MODIFIED or state == EXCLUSIVE or state == SHARED):

                    self.hitAlert = 1

                    # hit
                    return 1

                #state I
                else:

                    self.missAlert = 1

                    # miss
                    return 0

            # no memory direction match
            else:

                return 0

    """
    
    """
    def localWrite(self, instruction):
        pass

    """
    This functions identifies the current instruction
    """
    def localSearch(self, instruction):

        # read operation
        if(instruction.getOperation() == OPERATIONS[READ_INDEX]):

            result = self.localRead(instruction)

        # write operation
        elif(instruction.getOperation() == OPERATIONS[WRITE_INDEX]):
    
            result = self.localWrite(instruction)

        # calc instruction
        else:

            result = 1

        return result












    """
    This function checks if the other caches have the requested block to read it
    """
    def remoteRead(self, instruction, bus):
        
        # acquire lock
        bus.acquireLock()

        memoryDirection = instruction.getMemoryDirection()

        cpuArray = bus.getCpuArray()

        currentCpu = cpuArray[instruction.getCpuNumber()]

        for cpu in cpuArray:

            # not check current CPU cache
            if(cpu.getNumber() != currentCpu.getNumber()):

                controller = cpu.getController()

                cache = controller.getCache()

                blocks = cache.getBlocks()

                for block in blocks:

                    # memory direction match
                    if(block.getMemoryDirection() == memoryDirection):

                        state = block.getState()

                        # not state I
                        if(state != "I"):

                            blockNumber = block.getNumber()

                            currentController = currentCpu.getController()

                            currentCache = currentController.getCache()

                            currentBlocks = currentCache.getBlocks()

                            currentBlock = currentBlocks[blockNumber]

                            value = block.getValue()                            

                            block.setState("S")                                

                            currentBlock.setState("S")

                            currentBlock.setMemoryDirection(memoryDirection)

                            currentBlock.setValue(value)

                    # search in main memory
                    else:

                        mainMemory = bus.getMainMemory()

                        dictionary = mainMemory.getDictionary()

                        value = dictionary.get(memoryDirection)

                        # change state to E ??????????????????????????????????????????????????????????

                        
















        # release lock
        bus.releaseLock()








        pass

    """
    
    """
    def remoteWrite(self, instruction):
        pass


    """
    
    """
    def remoteSearch(self, instruction):
        pass


    """
    
    """
    def remoteSearch(self, instruction, bus):
        
        # read operation
        if(instruction.getOperation() == OPERATIONS[READ_INDEX]):

            result = self.remoteRead(instruction, bus)

        # write operation
        elif(instruction.getOperation() == OPERATIONS[WRITE_INDEX]):
    
            result = self.remoteWrite(instruction, bus)

        # calc instruction
        else:

            result = 1

        return result




























    def invalidateCaches(self):
        pass

class CPU:
    
    def __init__(self, number):        
        self.number = number        
        self.currentInstruction = None
        self.controller = None

        self.assignResources()

    def getNumber(self):
        return self.number

    def setNumber(self, number):
        self.number = number

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

            return OPERATIONS[CALC_INDEX]

        elif(probability >= CALC_PROBABILITY and probability < READ_PROBABILITY):

            return OPERATIONS[READ_INDEX]

        else:

            return OPERATIONS[WRITE_INDEX]

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
    This function assign controller and cache to the CPU
    """
    def assignResources(self):
        
        # create controller
        controller = Controller()

        # create cache
        cache = Cache()

        # assign cache blocks to the cache **************************************************************** NO SE SABE SI ES ASI
        for i in range(0, 4):
        
            memoryIndex = randint(0, 7)

            cacheBlock = CacheBlock(i, INITIAL_CACHE_STATE, MEMORY_BLOCKS_DIR[memoryIndex], 0)

            cache.blocks.append(cacheBlock)

        # assign cache to controller
        controller.setCache(cache)

        # assign controller to CPU        
        self.controller = controller

    """
    This function generates a new instruction for the received CPU
    """
    def generateInstruction(self):        
        
        operation = self.getOperation(self.poissonDistribution())

        instruction = Instruction(self.cpuNumber, operation)

        # not calc operation
        if(operation != OPERATIONS[CALC_INDEX]):
            
            memoryDirection = self.getMemoryDirection(self.poissonDistribution())

            instruction.setMemoryDirection(memoryDirection)

            # write operation
            if(operation == OPERATIONS[WRITE_INDEX]):
            
                value = self.getValue()

                instruction.setValue(value)
        
        self.currentInstruction = instruction

    """
    This functions allows the CPU and controller to execute a new instruction 
    """
    def executeInstruction(self, bus):

        self.resetAlerts()

        localSearch = self.controller.localSearch(self.currentInstruction)

        # miss
        if(localSearch == 0):

            remoteRead = self.remoteSearch(self.currentInstruction, bus)
























    """
    This function indicates to the CPU to generate and execute a new instruction
    """
    def threadFunction(self, bus):
        
        self.generateInstruction()

        self.executeInstruction(bus)

        #pass