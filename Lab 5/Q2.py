#Write a program using While Loop to compute the factorial of a number.
n = int(input("Enter a number: "))
i = 1
fact = 1
if n == 0:
    fact = fact
else:
    while n >= i:
        fact = fact*i
        i = i + 1
print("Factoral:", fact)   

