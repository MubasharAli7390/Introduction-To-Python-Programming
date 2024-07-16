#find common elements in two lists
a = [1,2,3,4,5,6]
b = [1,3,8,8,9,0]
li = ""
c = a
d = b
for i in a:
    for j in b:
        if j == i:
            li = li + " " + str(j)
            j = j + 1
    i = i + 1
print("common elements:",li)
