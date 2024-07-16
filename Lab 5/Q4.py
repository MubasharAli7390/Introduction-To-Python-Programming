#Write a program using a nested while loop to print a square of asterisks.
i = 4
n = 0
while n <= i:
    j = 0
    while j <= i:
        print("*", end="")
        j = j + 1
    n = n +1
    print('')