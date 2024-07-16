#Write a Python program to generate a 3*4*6 3D array whose each element is *
A1 = []
for i in range (1,4):
    A2 = []
    for j in range(1,5):
        A3 = []
        for k in range (1,7):
            A3.append("*")
        A2.append(A3)
    A1.append(A2)

print(A1)
