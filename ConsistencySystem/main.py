# libraries
#from functions import *
from threading import *
from models import *

# create CPUs
cpu0 = CPU(0)
cpu1 = CPU(1)
cpu2 = CPU(2)
cpu3 = CPU(3)

# create CPUs array
cpuArray = [cpu0, cpu1, cpu2, cpu3]

# create main memory
mainMemory = MainMemory()

# create bus
bus = Bus(cpuArray, mainMemory)

# create threads
thread0 = Thread(target = cpu0.threadFunction, args=(bus,))
thread1 = Thread(target = cpu1.threadFunction, args=(bus,))
thread2 = Thread(target = cpu2.threadFunction, args=(bus,))
thread3 = Thread(target = cpu3.threadFunction, args=(bus,))

# start threads
thread0.start()
thread1.start()
thread2.start()
thread3.start()

# wait until threads are completely executed
thread0.join()
thread1.join()
thread2.join()
thread3.join()



"""
for i in cpu0.controller.cache.blocks:
    print(i.getNumber())
    print(i.getState())
    print(i.getMemoryDirection())
    print(i.getValue())
    print("")
"""

"""
for cpu in cpuArray:
    print(cpu.currentInstruction.operation)
"""

#print(mainMemory.dictionary)
