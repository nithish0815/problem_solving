s_username="EMC"
s_password="123"

uname=input("Enter your username:")
password=input("Enter the password:")
def validate():
    if (s_username==uname and s_password==password):
        return True
    else:
        return False
a=validate()
print(a)
