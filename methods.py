# types of methods
"""
 working with class
1, create a class
2,initialize or constructor
3,create object
4, create methods

  3 types of methods
    1,instance methods
    2,class methods
    3,static methods
"""


class student:
    school = "RDM"  # outside the instance

    # instance variable use with instance methods
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print("this is a student")


s1 = student(2, 4, 6)
s2 = student(8, 6, 1)

print(s1.avg())
print(s2.avg())
print(student.getschool())
student.info()
"""
# gettors get the value
    def get_m1(self):
        return self.m1
    # SETTORS set the value 
    def set_m1(self):
        self.m1 = 4  # value

"""
