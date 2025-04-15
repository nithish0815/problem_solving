def alpha(s):
    result=""
    for char in s:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
            result += char
    return  result
s= "HELLO world 123*^%$#%R&$$"
print(alpha(s))
alpha(s)