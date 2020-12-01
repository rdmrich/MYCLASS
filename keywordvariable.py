# scope
a = 5
print(id(a))


def cach():
    a = 6
    x = globals()['a']
    print(id(x))
    print("in fun", a)

    globals()['a'] = 15


cach()
print("outside", a)


def person(name, **data):
    print(name)
    for i, j in data.items():
        print(i, j)


person('rich', age=20, phone=778203873,
       city='Goma')


# pass list to a function
def count():
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


for i in range(3):
    lst = [int(input("enter a number even or odd"))]
    i += 1
    even, odd = count()
print(even)
print(odd)
