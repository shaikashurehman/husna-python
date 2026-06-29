try:
    age=int(input("enter age"))
    if age%2==0:
       print("even")
    else:
        print("odd")
except valueError:
    print("value error")