# libraries
from threading import *
from models import *


from constants import *




# create CPUs
cpu0 = CPU(0)
cpu1 = CPU(1)
cpu2 = CPU(2)
#cpu3 = CPU(3)

"""
# create CPUs array
cpuArray = [cpu0, cpu1, cpu2, cpu3]

# create main memory
mainMemory = MainMemory()

# create bus
bus = Bus(cpuArray, mainMemory)
"""






# VALORE QUEMADOS

# cpu0
# block0
cpu0.controller.cache.blocks[0].state = SHARED
cpu0.controller.cache.blocks[0].memoryDirection = MEMORY_BLOCKS_DIR[0]
cpu0.controller.cache.blocks[0].value = hex(10)
# block1
cpu0.controller.cache.blocks[1].state = SHARED
cpu0.controller.cache.blocks[1].memoryDirection = MEMORY_BLOCKS_DIR[6]
cpu0.controller.cache.blocks[1].value = hex(34)
# block2
cpu0.controller.cache.blocks[2].state = MODIFIED
cpu0.controller.cache.blocks[2].memoryDirection = MEMORY_BLOCKS_DIR[5]
cpu0.controller.cache.blocks[2].value = hex(8)
# block3
cpu0.controller.cache.blocks[3].state = MODIFIED
cpu0.controller.cache.blocks[3].memoryDirection = MEMORY_BLOCKS_DIR[3]
cpu0.controller.cache.blocks[3].value = hex(30)

# cpu1
# block0
cpu1.controller.cache.blocks[0].state = INVALID
cpu1.controller.cache.blocks[0].memoryDirection = MEMORY_BLOCKS_DIR[0]
cpu1.controller.cache.blocks[0].value = hex(30)
# block1
cpu1.controller.cache.blocks[1].state = INVALID
cpu1.controller.cache.blocks[1].memoryDirection = MEMORY_BLOCKS_DIR[2]
cpu1.controller.cache.blocks[1].value = hex(34)
# block2
cpu1.controller.cache.blocks[2].state = INVALID
cpu1.controller.cache.blocks[2].memoryDirection = MEMORY_BLOCKS_DIR[3]
cpu1.controller.cache.blocks[2].value = hex(18)
# block3
cpu1.controller.cache.blocks[3].state = SHARED
cpu1.controller.cache.blocks[3].memoryDirection = MEMORY_BLOCKS_DIR[7]
cpu1.controller.cache.blocks[3].value = hex(38)

# cpu2
# block0
cpu2.controller.cache.blocks[0].state = MODIFIED
cpu2.controller.cache.blocks[0].memoryDirection = MEMORY_BLOCKS_DIR[2]
cpu2.controller.cache.blocks[0].value = hex(200)
# block1
cpu2.controller.cache.blocks[1].state = SHARED
cpu2.controller.cache.blocks[1].memoryDirection = MEMORY_BLOCKS_DIR[6]
cpu2.controller.cache.blocks[1].value = hex(34)
# block2
cpu2.controller.cache.blocks[2].state = INVALID
cpu2.controller.cache.blocks[2].memoryDirection = MEMORY_BLOCKS_DIR[7]
cpu2.controller.cache.blocks[2].value = hex(108)
# block3
cpu2.controller.cache.blocks[3].state = INVALID
cpu2.controller.cache.blocks[3].memoryDirection = MEMORY_BLOCKS_DIR[3]
cpu2.controller.cache.blocks[3].value = hex(28)

# create CPUs array
cpuArray = [cpu0, cpu1, cpu2]

# create main memory
mainMemory = MainMemory()

# create bus
bus = Bus(cpuArray, mainMemory)

# mainMemory
mainMemory.dictionary[MEMORY_BLOCKS_DIR[0]] = hex(10)
mainMemory.dictionary[MEMORY_BLOCKS_DIR[1]] = hex(34)
mainMemory.dictionary[MEMORY_BLOCKS_DIR[2]] = hex(8)
mainMemory.dictionary[MEMORY_BLOCKS_DIR[3]] = hex(28)
mainMemory.dictionary[MEMORY_BLOCKS_DIR[4]] = hex(8)
mainMemory.dictionary[MEMORY_BLOCKS_DIR[5]] = hex(34)
mainMemory.dictionary[MEMORY_BLOCKS_DIR[6]] = hex(34)
mainMemory.dictionary[MEMORY_BLOCKS_DIR[7]] = hex(38)

# N1: READ 000
instruction = Instruction(1, OPERATIONS[READ_INDEX])
instruction.memoryDirection = MEMORY_BLOCKS_DIR[0]
cpu1.currentInstruction = instruction
cpu1.executeInstruction(bus)

cpu1.controller.resetAlerts()

# N0: WRITE 000, 0110
instruction = Instruction(0, OPERATIONS[WRITE_INDEX])
instruction.memoryDirection = MEMORY_BLOCKS_DIR[0]
instruction.value = hex(110)
cpu0.currentInstruction = instruction
cpu0.executeInstruction(bus)

cpu0.controller.resetAlerts()

# N1: READ 010
instruction = Instruction(1, OPERATIONS[READ_INDEX])
instruction.memoryDirection = MEMORY_BLOCKS_DIR[2]
cpu1.currentInstruction = instruction
cpu1.executeInstruction(bus)

cpu1.controller.resetAlerts()

# N2: READ 111
instruction = Instruction(2, OPERATIONS[READ_INDEX])
instruction.memoryDirection = MEMORY_BLOCKS_DIR[7]
cpu2.currentInstruction = instruction
cpu2.executeInstruction(bus)

cpu2.controller.resetAlerts()

# N0: WRITE 001, 0089
instruction = Instruction(0, OPERATIONS[WRITE_INDEX])
instruction.memoryDirection = MEMORY_BLOCKS_DIR[1]
instruction.value = hex(89)
cpu0.currentInstruction = instruction
cpu0.executeInstruction(bus)

cpu0.controller.resetAlerts()

# N1: READ 111
instruction = Instruction(1, OPERATIONS[READ_INDEX])
instruction.memoryDirection = MEMORY_BLOCKS_DIR[7]
cpu1.currentInstruction = instruction
cpu1.executeInstruction(bus)



"""
# create threads
thread0 = Thread(target = cpu0.threadFunction, args=(bus,))
#thread1 = Thread(target = cpu1.threadFunction, args=(bus,))
#thread2 = Thread(target = cpu2.threadFunction, args=(bus,))
#thread3 = Thread(target = cpu3.threadFunction, args=(bus,))

# start threads
thread0.start()
#thread1.start()
#thread2.start()
#thread3.start()

# wait until threads are completely executed
thread0.join()
#thread1.join()
#thread2.join()
#thread3.join()
"""

"""
a = "0b0101"
b = int(a, 2)
print(a)
print(b)
print(b % 4)

#print(f'{0b101:#0}')
"""

"""
for i in cpu0.controller.cache.blocks:
    print(i.getNumber())
    print(i.getState())
    print(i.getMemoryDirection())
    print(i.getValue())
    print("")
"""

print("")

print("N 0")
print("Hit:", cpu0.controller.hitAlert)
print("Miss:", cpu0.controller.missAlert)
print("-----------------------------------------------")

print("N 1")
print("Hit:", cpu1.controller.hitAlert)
print("Miss:", cpu1.controller.missAlert)
print("-----------------------------------------------")

print("N 2")
print("Hit:", cpu2.controller.hitAlert)
print("Miss:", cpu2.controller.missAlert)
print("-----------------------------------------------")

print("-----------------------------------------------")

for cpu in cpuArray:
    print("N", cpu.number)
    for block in cpu.controller.cache.blocks:
        print("B", block.number)
        print("State:", block.state)
        print("Dir:", block.memoryDirection)
        print("Value:", block.value)
        print("")
    print("-----------------------------------------------")

print(mainMemory.dictionary)
print("")


"""
print(MEMORY_BLOCKS_DIR)
"""

"""
print(0 % 4)
print("")
"""
