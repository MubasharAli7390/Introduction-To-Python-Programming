#Calculating the factorial of a number using python function.
value = int(input("Enter a number: "))
def factorial(n):
    a = 1
    for i in range(1,n+1):
        a = a*i
    return a 

print("factorial: ",factorial(value))
