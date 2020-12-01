class student:

    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name, self.age, self.rollno)
        self.lap.show()
    # inner class
    class laptop:

        def __init__(self):
            self.brand = "hp"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = student("rich", 20, 2)
s2 = student("amos", 21, 4)

s1.show()

# lap1 = student.laptop()
# lap1.show()
