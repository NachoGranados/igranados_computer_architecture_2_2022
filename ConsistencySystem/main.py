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
cpu0.cache = cache0
cpu1.cache = cache1
cpu2.cache = cache2
cpu3.cache = cache3

# assign each block to each cache
assignCacheBlocks(cpu0)
assignCacheBlocks(cpu1)
assignCacheBlocks(cpu2)
assignCacheBlocks(cpu3)

# create main memory
mainMemory = MainMemory()

# create threads
t0 = Thread(target = threadFunction, args=(cpu0,))
t1 = Thread(target = threadFunction, args=(cpu1,))
t2 = Thread(target = threadFunction, args=(cpu2,))
t3 = Thread(target = threadFunction, args=(cpu3,))

# start threads
t0.start()
t1.start()
t2.start()
t3.start()

# wait until threads are completely executed
t0.join()
t1.join()
t2.join()
t3.join()
