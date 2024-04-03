'''Write a program that allows the user to enter a string then:¶

If the length of the string is less than 2 , give an error message

Otherwise make a new string that is made from 4 copies of the last two characters

Print the new string

Input: the

Output: hehehehe'''

str = input("Enter a string: ")
if len(str) < 2:
    print("The length of given string is less than 2")
else:
    twoChar = str[-2:]
    print(twoChar + twoChar + twoChar + twoChar)