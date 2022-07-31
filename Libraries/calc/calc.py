import time

class Calc():
    def __init__(self):
        print("initializing calc...")
        time.sleep(5) # simulating time taken to initialize a hardware
        print("calc initialization done")

    def add(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return self.num1+self.num2

    def sub(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return num1-num2

    def mult(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return num1*num2

    def power(self, num1,num2):
        self.num1 = num1
        self.num2 = num2
        print(f"printing the result of add and sub: {self.add(num1, num2)} {self.sub(num1, num2)}")
        return pow(num1,num2)

    def all_result(self, num1, num2):
        return [self.add(num1, num2), self.sub(num1, num2), self.power(num1, num2)]