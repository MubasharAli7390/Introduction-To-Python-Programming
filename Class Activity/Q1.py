#Write a user defined function to calculate the area of a rectangle
a = int(input("Enter the length: "))
b = int(input("Enter the width: "))

def rectangle(l,w):
    r = l * w
    return r
print(rectangle(a,b))
