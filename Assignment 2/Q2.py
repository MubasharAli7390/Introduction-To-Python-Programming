#2.Write a Python program to shuffle and print a specified list.
list = [1,2,3,4,5,6,7,8,9,10]
def listShuffle(n):
    a = n.pop(3)
    b = n.pop(1)
    c = n.pop(6)
    d = n.pop(5)
    n.insert(0,a)
    n.insert(5,b)
    n.insert(10,c)
    n.insert(5,d)
    return n
print(listShuffle(list))