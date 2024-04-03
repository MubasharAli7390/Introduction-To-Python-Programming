'''Change a string to uppercase with a test

Write a program to that allows the user to enter a string

Change all the characters to uppercase if there at least two uppercase characters in the first 4'''

string = input("Enter a string: ")
length = len(string)
chr = 0
if string[0].upper() == string[0]:
    chr = chr + 1
if length >= 2:    
    if string[1].upper() == string[1]:
        chr = chr + 1
if length >= 3:   
    if string[2].upper() == string[2]:
        chr = chr + 1
if length >= 4:    
    if string[3].upper() == string[3]:
        chr = chr + 1
if chr >= 2:
    print(string.upper())
else: 
    print(string)