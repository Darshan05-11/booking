s_username="emc"
s_password="123"
uname=input("enter the name")
password=input("enter the password")

def validate():
    if(s_username==uname and s_password==password):
        return True
    else:
        return False
a=validate()
print(a)

def add(n1,n2):
    return n1+n2
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
added=add(a,b)
output=added*c
print(output)