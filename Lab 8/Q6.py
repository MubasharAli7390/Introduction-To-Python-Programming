#Calculate the product of two numbers using anonymous functions.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = lambda m,n: m*n
product = c(a,b)
print(product)