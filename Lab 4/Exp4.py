#Determining the largest of three numbers using nested if statements.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a > b:
    if a > c:
        print("first number is the highest")
    else:
         print("third number is the largest")
elif b > a:
        if b > c:
            print("second number is the highest")
        else:
             print("third number is the largest")
