#Determining the highest among three numbers.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a > b and a > c:
    print("first number is the highest")
elif b > a and b > c:
    print("second number id the highest")
else:
    print("third number is the highest")