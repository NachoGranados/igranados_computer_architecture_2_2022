from random import *
from constants import *
from models import *

def assignCacheBlocks(processor):

    memoryIndex = randint(0, 7)

    processor.cache.block0 = CacheBlock(0, INITIAL_CACHE_STATE, MEMORY_BLOCKS_DIR[memoryIndex], 0)

    memoryIndex = randint(0, 7)

    processor.cache.block1 = CacheBlock(1, INITIAL_CACHE_STATE, MEMORY_BLOCKS_DIR[memoryIndex], 0)

    memoryIndex = randint(0, 7)

    processor.cache.block2 = CacheBlock(2, INITIAL_CACHE_STATE, MEMORY_BLOCKS_DIR[memoryIndex], 0)

    memoryIndex = randint(0, 7)

    processor.cache.block3 = CacheBlock(3, INITIAL_CACHE_STATE, MEMORY_BLOCKS_DIR[memoryIndex], 0)