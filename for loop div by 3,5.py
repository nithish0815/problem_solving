n = int(input("enter the the value:"))
count=0
for i in range(1,n+1):
    if(i%3 == 0 and i%5 == 0):
        count=count+1
print(count)