# libraries
from functions import *
from threading import *
from models import *

# create processors
p0 = Processor(0)
p1 = Processor(1)
p2 = Processor(2)
p3 = Processor(3)

# create threads
t0 = Thread(target = threadFunction, args=(p0,))
t1 = Thread(target = threadFunction, args=(p1,))
t2 = Thread(target = threadFunction, args=(p2,))
t3 = Thread(target = threadFunction, args=(p3,))

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
