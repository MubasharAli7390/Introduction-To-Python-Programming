"""Write a program using nested for Loop to printing a pattern of alternating characters.
A
AB
ABA
ABAB
ABABA
"""

for i in range(1,6):
  for j in range(i):
    print(chr(65 + j % 2), end="")
  print()


