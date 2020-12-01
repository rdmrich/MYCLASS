class computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is ", self.cpu, self.ram)


comp1 = computer('i5', '8gb')
comp2 = computer('amd5', '16gb')
# calling a method or a function
comp1.config()
comp2.config()
