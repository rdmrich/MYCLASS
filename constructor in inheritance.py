# constructor
class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")


class B(A):

    def __init__(self):
        print("in B init")

    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working")


a1 = B()