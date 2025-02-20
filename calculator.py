class Calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("add:",self.num1+self.num2)

obj1=Calculator(10,2)
obj1.add()