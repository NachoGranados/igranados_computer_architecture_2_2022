# libraries
from constants import *
from functions import *
class Processor:
    
    def __init__(self, number):        
        self.number = number
        #self.instructions = []
        #self.controller = controller
        #self.cache = cache

class Instruction:
    
    def __init__(self, processorNumber, operation):        
        self.processorNumber = processorNumber
        self.operation = operation
        self.memoryDirection = None
        self.value = None

    def getProcessorNumber(self):
        return self.processorNumber

    def setProcessorNumber(self, processorNumber):
        self.processorNumber = processorNumber

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
