# arguments
""" Actual Argument
has position, keyword, default
 variable length """


def person(name, age=18):
    print(name)
    print(age)


person('rich', 20)


def sum(a, *b):
    c = a
    for i in b:
        c = c + 1
    return c

    print(c)
sum(2, 7, 1, 4)



# pass values
def create(x):
    print(id(lst))
    lst[1] = 6
    print('x', lst)


lst = [1, 2, 3]
print(id(lst))
create(lst)
print('list', lst)


# functions
def add_sub(x, y):
    z = x + y
    t = x - y
    return z, t


result_sub, result_add = add_sub(3, 5)
print(result_add, result_sub)


def greet():
    print("hello")
    print("good morning")


def add(x, y):
    z = x + y
    return z


greet()
result = add(2, 4)
print(result)
