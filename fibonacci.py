# fibonacci sequence
def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n < 0:
        print("negative number")
    else:
        print(a)
        print(b)

    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)


fib(6)


# factorial number
def fact(t):
    f = 1
    for i in range(1, t + 1):
        f = f * i
    return f


x = 5
result = fact(x)
print(result)
