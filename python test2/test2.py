def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def division(a,b):
    return(a/b)
print("enter ur choice")
print("1.add 2.subtract 3.multiply 4.division")
a=int(input("enter the number1"))
b=int(input("enter the number2"))
choice=int(input("enter ur choice"))
if choice==1:
    print("addition:",add(a,b))
elif choice==2:
    print("subtraction:",subtract(a,b))
elif choice==3:
    print("multiply:",multiply(a,b))
elif choice==4:
    print("division:",division(a,b))
else:
    print("invalid choice")