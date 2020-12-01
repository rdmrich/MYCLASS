"""
duck typing in python
"""

class pycharm:
    def execute(self):
        print('compiling')
        print('running')


class myeditor:

    def execute(self):
        print('spell my code')
        print('conversion checker')


class laptop:

    def code(self, ide):
        ide.execute()


#ide = pycharm()
ide = myeditor()
lap1 = laptop()
lap1.code(ide)
"""
methode overriding
"""


class student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1, m2)

        return s3

    # greater than gt
    def __gt__(self, other):
        r1 = self.m1 + other.m1
        r2 = self.m2 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = student(1, 6)
s2 = student(7, 3)
s3 = s1 + s2
if s1 > s2:
    print('true')
else:
    print('false')
print(s3.m2)

print(s1)
print(s2)


# method overloading

class studen:

    def __init__(self, m, m3):
        self.m = m
        self.m3 = m3

    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            a = a + b + c
        elif a != None and b != None:
            a = a + b
        else:
            a = a
        return a


a1 = studen(3, 2)

print(a1.sum(3, 4))

"""
methode overriding
"""


class A:
    def show(self):
        print('in a show')


# ovverriding a
class B(A):
    def show(self):
        print('in b show')


b1 = B()
b1.show()
