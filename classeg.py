class student:
    def __init__(self):
        self.name="name"
        self.regno="108"
    def display(self):
        print("Name:",self.name)
        print("Regno:",self.regno)
s1=student()
s2=student()

s1.name="Manoj"
s1.regno="1"
s2.name="Karthi"
s2.regno="2"

s1.display()
s2.display()