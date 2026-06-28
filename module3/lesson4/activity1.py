#using a try and except

#try:

#input a number

# #print the number

#using value error

# except the value error and print the exception

#except ValueError as ex:

# print("Exception:", ex)
try:
    i=int(input("enter a number"))
    print(i)
except ValueError as ex:
    print("Exception:", ex)


