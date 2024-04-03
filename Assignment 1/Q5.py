'''Replacing letters in a string

Write a program that for a given string, all occurrences of its first character have been changed to '$', except the first character itself.

Test your program using the word agama (a species of lizard)

Print the original string and the new string
'''

str = input("Enter a string: ")
replace_char = str[0]
sliced_str = str[1::]
new_s = sliced_str.replace(replace_char, "$")
print(str)
print(replace_char + new_s)