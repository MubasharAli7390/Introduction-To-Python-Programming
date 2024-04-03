#Write a program that uses a simple if statement to check multiple conditions using logical operators.
a = int(input("Enter a number: "))
if a > 5 and a < 100:
    print("A is greater than five and a is less than 100")
if a == 10 or a == 20:
    print("A is equal to 10 or A is equal to 20")
if not(a < 0):
    print("A is positive")