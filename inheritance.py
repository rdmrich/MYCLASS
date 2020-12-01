class A:

    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")


"""
inheritance
child class or subclass 
class B is inheriting 
all the features from A

"""


# single level inheritance
class B(A):

    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working")


# multi level inheritance
class C(B):

    def feature5(self):
        print("feature 5 is working")

    def feature6(self):
        print("feature 6 is working")


# multiple inheritance
class D():

    def feature7(self):
        print("feature  7 is working")


class E():

    def feature8(self):
        print("feature 8 is working")


class F(D, E):

    def feature(self):
        print("feature  is working")


a1 = A()
a1.feature1()
a1.feature2()
b = B()
b.feature3()
b.feature1()
c = C()
c.feature5()
f = F()
f.feature7()