#Write a Python program to find the index of an item in a specified lists
user_input = str(input("Enter the item whose index you want to find:"))
specifiedList = ["Computer","Mouse","Keyboard","Monitor"]
def findIndex(n):
    return specifiedList.index(n)

print(findIndex(user_input))

    