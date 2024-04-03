'''String reverse¶

Allow the user to input a string

If it’s a multiple of 4 reverse the string

Otherwise give a suitable error message'''

str = input("Enter a string: ")
str_int = int(str)
str_len = len(str)-1
if str_int % 4 == 0:
    print(str[::-1])
else:
    print("Not a multiple of 4")