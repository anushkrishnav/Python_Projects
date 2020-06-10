def validate(name):
    numbererror="Your name must be atleast 8 characters"
    charerror="Your name must contain only alphabets"
    if len(name)<8:
        return numbererror
    else :
        if name.isalpha():
            success="Validation success"
            return success
        else:
            return charerror

name=str(input("Please enter the name to validate \n "))
print(validate(name))
'''
#swap 2 numbers 
x=int(input("Enter x value\n"))

y=int(input("Enter y value\n"))

print("\n Before Swap\n")
print("x=",x)
print("\ny=",y)
#swapping without using a third variable
x=x+y
y=x-y
x=x-y

print("\n After Swap\n")
print("x=",x)
print("\ny=",y)'''