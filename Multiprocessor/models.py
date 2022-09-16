# libraries
from constants import *
from functions import *
class Processor:

    def __init__(self, number):        
        self.number = number

    def generateInstruction(self):
        
        processorNumber = "P" + str(self.number) + ": "

        instruction = getInstruction(poissonDistribution())

        # calc instruction
        if(instruction == OPERATIONS[0]):

            return processorNumber + instruction

        # read instruction
        elif(instruction == OPERATIONS[1]):

            memoryDir = " " + getMemoryDirection(poissonDistribution())

            return processorNumber + instruction + memoryDir

        # write operation
        elif(instruction == OPERATIONS[2]):

            memoryDir = " " + getMemoryDirection(poissonDistribution()) + "; "

            value = getValue()

            return processorNumber + instruction + memoryDir + value

    def executeInstruction(self):
        pass

################################################################################

class Instruction:
    
    def __init__(self, processorNumber, operation, memDirection, value):        
        self.processorNumber = processorNumber
        self.operation = operation
        self.memDirection = memDirection # in case of write
        self.value = value # in case of write

    def getProcessorNumber(self):
        return self.processorNumber

    def setProcessorNumber(self, processorNumber):
        self.processorNumber = processorNumber

    def getOperation(self):
        return self.operation

    def setOperation(self, operation):
        self.operation = operation

    def getMemDirection(self):
        return self.memDirection

    def setMemDirection(self, memDirection):
        self.memDirection = memDirection

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
