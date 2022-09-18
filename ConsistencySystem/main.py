# libraries
from ConsistencySystem.functions import *
from threading import *
from ConsistencySystem.models import *

# create processors
processor0 = Processor(0)
processor1 = Processor(1)
processor2 = Processor(2)
processor3 = Processor(3)

# create caches for each processor
cache0 = Cache(0)
cache1 = Cache(1)
cache2 = Cache(2)
cache3 = Cache(3)

# assign each cache to the respective processor
processor0.cache = cache0
processor1.cache = cache1
processor2.cache = cache2
processor3.cache = cache3

# assign each block to each cache
assignCacheBlocks(processor0)
assignCacheBlocks(processor1)
assignCacheBlocks(processor2)
assignCacheBlocks(processor3)

# create main memory
mainMemory = MainMemory()

# create threads
t0 = Thread(target = threadFunction, args=(processor0,))
t1 = Thread(target = threadFunction, args=(processor1,))
t2 = Thread(target = threadFunction, args=(processor2,))
t3 = Thread(target = threadFunction, args=(processor3,))

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
