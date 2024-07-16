""" print the following
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""
r = 5
i = 0
while i <= r:
    j = 1
    while j <= i:
        print(j, end=" ")
        j = j + 1
    i = i + 1
    print('')
