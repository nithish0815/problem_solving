def nth_term_ap(a,d,n):
    return a + (n - 1) * d

a = int(input("enter the value of (a):"))
d = int(input("enter the value of (d):"))
n = int(input("enter the value of (n):"))

value = nth_term_ap(a,d,n)
print(value)
