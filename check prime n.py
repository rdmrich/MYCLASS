from array import *
# array
vals = array('i', [2, 3, 4, 9, 7])
newArr = array(vals.typecode, (e*e for e in vals))

for a in newArr:
    print(a)
    print()
for i in range(5):
    print(vals[i])
print(vals.typecode)
print(vals.buffer_info())

# example
arr = array('i', [])
n = int(input("enter the length of the array"))
for i in range(n):
    x = int(input("Enter the next value"))
    arr.append(x)
    print(arr)

val = int(input("Enter the value for search"))
k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k += 1
print(arr.index(val))




# prime number
num = 10
for i in range(2, num):
    if num % i == 0:
        print("this is not a prime number")
        break
    else:
        print("prime")
