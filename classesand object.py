# classes and object
class Robot:
    def _init_(self, Name, height):
        self.name = name
        self.height = height

    def introduce_self(self):
        print("My name is " + self.name)


r1 = Robot()
r1.name = "rich"
r1.height = 160

r2 = Robot()
r2.name = "dush"
r2.heignt = 170

r1.introduce_self()
r2.introduce_self()
