'''Are you a Mr?¶

Write a program to check whether a string input by the user starts with Mr'''

string = input("Enter a string: ")
first = string[0:2]
if first == "Mr":
    print("The given string starts with Mr")
else:
    print("The given string does not starts with Mr")