n = int(input("enter the number:"))
list = []
sum = 0

for i in range(1,n):
    if n%i == 0:
        list.append(i)
for i in list:
    sum = sum+i
if sum == n:
    print("true")
else:
    print("false")
