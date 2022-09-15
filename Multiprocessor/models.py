class Processor:

    def __init__(self, number):        
        self.number = number
        
    def getNumber(self):
        return self.number

    def setNumber(self, number):
        self.number = number

    def generateProcessingInstruction(self):
        pass

    def generateCalcInstruction(self):
        pass

    def generateWriteInstruction(self):
        pass

    def generateReadInstruction(self):
        pass

    def test(self, message):
        print(message)

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
