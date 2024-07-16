#Write a Python program access the index of a list.
user_input = int(input("Enter the index: "))
specifiedList = ["Computer","Mouse","Keyboard","Monitor"]
def indexAccess(n):
    return specifiedList[n]

print("Element:",indexAccess(user_input))