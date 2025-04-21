def prime_num(n):
    count = 0
    for i in range(2,n):
      if n % i == 0:
            count += 1
    # print(count)
    if count == 0:
        return "Prime number"
    else:
        return "not prime num"


n = int(input("enter the value:"))
print(prime_num(n))


