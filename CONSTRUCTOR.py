class computer:
    def __init__(self):
        self.name = "rich"
        self.age = 20

    def update(self):
        self.age = 21

    def compare(self, other):
        # c2 = other
        # compare (who si calling, whom to compare)
        if self.age == other.age:
            return True
        else:
            return False


c1 = computer()
# c1.age = 56
c2 = computer()
if c1.compare(c2):
    print("they are the same")
else:
    print("they are not same")
c1.update()
