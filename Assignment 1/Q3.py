'''Changing the case of a sentence
Write a program to that allows the user to enter a sentence

Change the sentence to UPPERCASE, lowercase, Title case, Capitalise Each Word

Print the original string

Print the four different versions re-cased string
'''

string = input("Enter a string: ")
print("string:", string)
print("uppercase:" ,string.upper())
print("lowercase: " ,string.lower())
print("titlecase: ", string.title())
print("Capitalize Each Word: ", string.upper())