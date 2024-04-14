#Determining the type of a triangle based on its side lengths: Equilateral triangle, Isosceles triangle, Scalene triangle
a = float(input("Enter the length of first side: "))
b = float(input("Enter the length of second side: "))
c = float(input("Enter the length of third side: "))
if a == b == c:
    print("It is an equilateral triangle")
elif a == b != c or a == c != b or b == c != a:
    print("It is an Isosceles triangle")
else:
    print("It is an Scalene triangle")