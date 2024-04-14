#Checking if a number is divisible by both 2 and 3.
a = float(input("Enter the number: "))
if a % 2 == 0:
    if a % 3 == 0:
        print("Number is divisible by both 2 and 3")
    else:
        print("Number is not divisible by 3")
else:
    print("Number is not divisible by 2")