def find(n):
    res = [[1]]
    for i in range(n-1):
        tem = [0] + res[-1] + [0]


        temp_res = []
        for j in range(len(tem) - 1):

            temp_res.append(tem[j] + tem[j+1])
        res.append(temp_res)
    print(res)
print(find(10))