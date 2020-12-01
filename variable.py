class car:
    # class namespace
    wheels = 4

    # instance namespace variable
    def __init__(self):
        self.mil = 10
        self.comp = "nissan"


c1 = car()
c1.mil = 8
c2 = car()
car.wheels = 5

print(c1.comp, c1.mil, c1.wheels)
print(c2.comp, c2.mil, c2.wheels)
