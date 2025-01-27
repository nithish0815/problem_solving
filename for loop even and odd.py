n = int(input("enter :"))
odd=0
even=0

for i in range(1,n+1):
    if i%2 == 0 :
        even+=1
    else:
        odd+=1
print(even)
print(odd)
