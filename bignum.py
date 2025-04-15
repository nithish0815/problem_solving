a = int(input("Enter the number of A:"))
b = int(input("Enter the number of B:"))
c = int(input("Enter the number of C:"))

if a > b and a > c:
    print("Biggest number is:", a)
elif b > c:
    print("Biggest number is:", b)
else:
    print("Biggest number is:", c)
