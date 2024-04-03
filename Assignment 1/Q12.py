'''Write a program that allows the user to enter a string then:¶

If the length of the string is less than 3 , give an error message and print the input string

Otherwise, make a new string from the first three characters if the original string

Print the new string'''

str = input("Enter a string: ")
if len(str) < 3:
    print("The string " + str + " has less than 3 characters")
else:
    firstThreeCharacter = str[0:3]
    print(firstThreeCharacter)