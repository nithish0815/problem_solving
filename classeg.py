class student:
    def __init__(self,name,reg):
        self.name=name
        self.regno=reg
    def display(self):
        return (f"NAME:{self.name}\n"
               f"REG.NO: {self.regno}")

s1=student("nithish",12385)
print(s1.display())
# s2=student()
#
# s1.name="Manoj"
# s1.regno="1"
# s2.name="Karthi"
# s2.regno="2"
#
# s1.display()
# s2.display()