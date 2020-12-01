from numpy import *
m1 = matrix('1 2 3;6 4 5; 1 6 7')
m2 = matrix('2 3 4; 7 6 5; 8 3 1')
m = m1 + m2
print(m)

arr = array([
            [1, 2, 3],
            [4, 5, 6]
])

arr1 = arr.flatten()
arr2 = arr1.reshape(2, 2, 3)
print(arr.shape)
print(arr.size)

