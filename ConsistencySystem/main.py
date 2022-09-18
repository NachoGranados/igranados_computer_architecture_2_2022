# libraries
from functions import *
from threading import *
from models import *

# create CPUs
cpu0 = CPU(0)
cpu1 = CPU(1)
cpu2 = CPU(2)
cpu3 = CPU(3)

# create caches
cache0 = Cache(0)
cache1 = Cache(1)
cache2 = Cache(2)
cache3 = Cache(3)

# assign each cache to the respective CPU
cpu0.setCache(cache0)
cpu1.setCache(cache1)
cpu2.setCache(cache2)
cpu3.setCache(cache3)

# assign each block to each cache
assignCacheBlocks(cpu0)
assignCacheBlocks(cpu1)
assignCacheBlocks(cpu2)
assignCacheBlocks(cpu3)

# create controllers
controller0 = Cache(0)
controller1 = Cache(1)
controller2 = Cache(2)
controller3 = Cache(3)

# assign each controller to the respective CPU
cpu0.setController(cache0)
cpu1.setController(cache1)
cpu2.setController(cache2)
cpu3.setController(cache3)

# create main memory
mainMemory = MainMemory()

# create threads
thread0 = Thread(target = threadFunction, args=(cpu0,))
thread1 = Thread(target = threadFunction, args=(cpu1,))
thread2 = Thread(target = threadFunction, args=(cpu2,))
thread3 = Thread(target = threadFunction, args=(cpu3,))

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











for i in cpu0.cache.blocks:
    print(i.getNumber())
    print(i.getState())
    print(i.getMemoryDirection())
    print(i.getValue())
    print("")
