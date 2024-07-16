'''
Write a program using WHILE LOOP with ELSE to Count the number of digits in a number.
Description: Use a while loop to count the number of digits in a number. The loop runs as long as the number is greater than 0. Inside the loop, we increment the count by 1 and then divide the number by 10 using the integer division operator to remove the rightmost digit. After the loop completes, we print the final value of the count.
'''
d = 0
n = int(input("Enter a number: "))
if n == 0:
    d = 1
else:
    while n > 0:
        d = d + 1
        n = n // 10
print("Digits: ", d)
