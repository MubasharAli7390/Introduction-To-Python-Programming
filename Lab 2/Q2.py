#Write a program to implement two Assignment and comparisons operators in Python
A = float(input("Enter value of A: "))
B = float(input("Enter value of B: "))
print("A > B", A > B) 
print("A < B", A < B) 
print("A >= B", A >= B) 
print("A <= B", A <= B) 
print("A == B", A == B) 
print("A != B", A != B)  
A = B
print("A = B", A)
A += B
print("A += B", A)
A -= B
print("A -= B", A)
A *= B
print("A *= B", A)
A /= B
print("A /= B", A)
A %= B
print("A %= B", A)