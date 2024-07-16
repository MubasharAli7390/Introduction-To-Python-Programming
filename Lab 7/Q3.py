#find common elements between two list
def elements(a,b):
    li = ""
    c = a
    d = b
    for i in a:
        for j in b:
            if j == i:
                li = li + " " + str(j)
                j = j + 1
        i = i + 1
    return li

aa = [1,2,3,4,5,6]
bb = [1,3,8,8,9,0]
print("common elements:",elements(aa,bb))

