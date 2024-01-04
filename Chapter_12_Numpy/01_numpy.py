# Numpy takes less momery than the python list takes and it can be proven by the below program
'''
import numpy as np
import sys

l = range(1000)
print(sys.getsizeof(5)*len(l))

array = np.arange(1000)
print(array.size*array.itemsize)
'''

# Numpy is also less time consumption than the python list

import numpy as np
import time
import sys

SIZE = 1000000

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

#python list
start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print("python list took: ",(time.time()-start)*1000)

#numpy array
start = time.time()
result = a1 + a2
print("numpy took: ",(time.time()-start)*1000)