from decorators import *
from factusingrecursion import fact


def main():
    print("name")
    print("Hello")


# this will hold the name  of the module
if __name__ == '__main__':
    main()


# another example
def func1():
    div(4, 6)
    print("from func1")


def func2():
    fact(5)
    print("from func2")


def main():
    func1()
    func2()


main()
# modules read different files
