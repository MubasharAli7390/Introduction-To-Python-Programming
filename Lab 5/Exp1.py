"""print a the following 
*
**
***
****
"""
r = 5
i = 0
while i < r:
    j = 0
    while j < i:
        print('*', end="")
        j = j + 1
    i = i + 1
    print('')

