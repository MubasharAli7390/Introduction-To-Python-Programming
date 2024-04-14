#Write a program that Input values from user than perform all arithmetic operations using if elif statements.

n1 = float(input("First number: "))
opr = input("Operator: ")
n2 = float(input("Second number: "))

if opr == "+":
    result = n1 + n2
elif opr == "-":
    result = n1 - n2
elif opr == "*":
    result = n1 * n2
elif opr == "/":
    result = n1 / n2
elif opr == "%":
    result = n1 % n2
else: 
    print("Invalid Operator")
print(result)

