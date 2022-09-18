# libraries
from constants import *
from functions import *

class CPU:
    
    def __init__(self, number):        
        self.number = number
        self.cache = None
        self.controller = None
        self.currentInstruction = None

    def getNumber(self):
        return self.number

    def setNumber(self, number):
        self.number = number

    def getCache(self):
        return self.cache

    def setCache(self, cache):
        self.cache = cache

    def getController(self):
        return self.controller

    def setController(self, controller):
        self.controller = controller

    def getCurrentInstruction(self):
        return self.currentInstruction

    def setCurrentInstruction(self, currentInstruction):
        self.currentInstruction = currentInstruction

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

class MainMemory:
    
    def __init__(self):        
        self.dictionary = None

    def getDictionary(self):
        return self.dictionary

    def setDictionary(self, dictionary):
        self.dictionary = dictionary

class Cache:
    
    def __init__(self, cpuNumber):
        self.cpuNumber = cpuNumber
        self.blocks = []

        #self.block0 = None
        #self.block1 = None
        #self.block2 = None
        #self.block3 = None

    def getCpuNumber(self):
        return self.cpuNumber

    def setCpuNumber(self, cpuNumber):
        self.cpuNumber = cpuNumber

    def getBlocks(self):
        return self.blocks

    def setBlocks(self, blocks):
        self.blocks = blocks

    """
    def getBlock0(self):
        return self.block0

    def setBlock0(self, block0):
        self.block0 = block0

    def getBlock1(self):
        return self.block1

    def setBlock1(self, block1):
        self.block1 = block1

    def getBlock2(self):
        return self.block2

    def setBlock2(self, block2):
        self.block2 = block2

    def getBlock3(self):
        return self.block3

    def setBlock3(self, block3):
        self.block3 = block3
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
    
    def __init__(self):
        pass

        #self.cpuNumber = cpuNumber    

    """
    def getCpuNumber(self):
        return self.cpuNumber

    def setCpuNumber(self, cpuNumber):
        self.cpuNumber = cpuNumber
    """
