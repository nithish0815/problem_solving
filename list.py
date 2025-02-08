list = [1,0,1,1,0,1,1,1]

count = 0
for i in range(len(list) - 1):
    if list[i] + list[i+1] == 2:
        count+=1
    else:
        pass
print(count)