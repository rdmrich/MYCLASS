from array import array
from numpy import *
# aliasing
arr2 = array([2, 6, 8, 9])
arr3 = arr1.copy()

arra = array([1, 2, 3, 4])
arr1 = arra + 5
print(arr1)
print(sin(arr1))
print(sum(arr1))
print(concatenate([arra, arr1]))
# ones
arr = ones([4])
# logspace
arr = logspace([1, 40, 5])
# arange()
arr = arange([1, 15, 3])
# linspace()
arr = linspace([1, 15, 3])
# array()
arr = array([1, 2, 3, 4.0], float)
print(arr.dtype)
