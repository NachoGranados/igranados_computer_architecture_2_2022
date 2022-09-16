# libraries
from functions import *
from threading import *
from models import *

# create processors
p1 = Processor(1)
p2 = Processor(2)
p3 = Processor(3)
p4 = Processor(4)

# create threads
t1 = Thread(target = threadFunction, args=(p1,))
t2 = Thread(target = threadFunction, args=(p2,))
t3 = Thread(target = threadFunction, args=(p3,))
t4 = Thread(target = threadFunction, args=(p4,))

# start threads
t1.start()
t2.start()
t3.start()
t4.start()

# wait until threads are completely executed
t1.join()
t2.join()
t3.join()
t4.join()
