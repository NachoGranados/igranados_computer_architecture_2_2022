from models import *
from functions import *

# create processors
processor0 = Processor(0)
processor1 = Processor(1)
processor2 = Processor(2)
processor3 = Processor(3)

#processorArray = [processor0, processor1, processor2, processor3]

# create caches for each processor
cache0 = Cache(0)
cache1 = Cache(1)
cache2 = Cache(2)
cache3 = Cache(3)

#cacheArray = [cache0, cache1, cache2, cache3]

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










