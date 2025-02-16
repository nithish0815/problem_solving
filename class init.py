class Teacher:
    def __init__(self,name,reg):
        self.name=name
        self.regno=reg
    def display(self):
        print("Name:",self.name)
        print("Reg no:",self.regno)
t1=Teacher("Thomas","1")
t2=Teacher("John","2")

t1.display()
t2.display()


