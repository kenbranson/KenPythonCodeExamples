import math
import numpy
import matplotlib.pyplot as plt

x = [1,2,15,3,6,17,8,16,8,3,10,12,16,12,9]

#some examples of using stats functions
print(numpy.min(x))
print(numpy.max(x))
print(numpy.std(x))
print(numpy.mean(x))
print(numpy.median(x))

# some examples of using plotting functions for graphs
plt.boxplot(x)
plt.show()

x = [2,3,4,5,7,9,13,15,17]
plt.plot(x)   #line chart
plt.ylabel('Sunlight')
plt.xlabel('Time')
plt.show()


import module_example as me
print(me.myFunction(7))