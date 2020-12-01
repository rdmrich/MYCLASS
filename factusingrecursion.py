from functools import reduce


# factorial using recursion its a function calling itself
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


if __name__:
    result = fact(5)
    print(result)

# Anonymous function
f = lambda a: a * a  # or a,b : a+b
result = f(8)
print(result)

# filter map reduce functions


nums = [2, 3, 5, 6, 7, 8, 9]
evens = list(filter(lambda n: n % 2 == 0, nums))
doubles = list(map(lambda n: n * 2, evens))
sum = reduce(lambda a, b: a + b, doubles)
print(evens)
print(doubles)
print(sum)
