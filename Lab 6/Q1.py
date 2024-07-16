'''
Write a program using nested for Loop to printing a pattern of characters in a right triangle:
A
BC
DEF
GHIJ
KLMNO
Hint: using the chr(ord(char) + 1) function to increment the alphabets.
'''

char = "A"
for i in range(1,6):
    for j in range(i):
      print(char, end="")
      char = chr(ord(char) + 1) 
    print()



