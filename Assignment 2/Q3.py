#Write a Python program to get the difference between the two lists.

def deffInLists(l1,l2):
    deff = []
    for i in l1:
        if i not in l2:
            deff.append(i)
    for j in l2:
        if j not in l1:
            deff.append(j)
    return deff

print(deffInLists([1,2,3,4],[2,1,5,2,7]))

