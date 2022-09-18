# libraries
from constants import *

class MainMemory:

    def __init__(self):        
        self.dictionary = self.startMemory()
        
    def startMemory(self):
        
        dictionary = {}

        for i in MEMORY_BLOCKS_DIR:

            dictionary[i] = hex(0)

        return dictionary
