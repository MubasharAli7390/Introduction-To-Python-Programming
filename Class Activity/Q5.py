#Write a lambda function to determine if a given number is odd
n = int(input("Enter a number: "))
oddOrNot = lambda a : "odd" if not(n%2 == 0) else "not odd"
print(oddOrNot(n))