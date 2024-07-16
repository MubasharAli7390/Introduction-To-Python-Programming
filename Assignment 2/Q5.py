#Write a Python program to convert a list of characters into a string.

def listToString(li):
    str = "";
    for i in li:
        str += i
    return str

print(listToString(['M','u','b','a','s','h','a','r']))