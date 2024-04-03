'''Write a program that allows the user to enter a string then:

If length of the string is less than 4 give an error message

add 'ing' at the end of a given string (length should be at least 3).

If the given string already ends with 'ing' then replace ing with 'ly' instead.

If the string length of the given string is less than 3, leave it unchanged. Sample String : 'abc' Expected Result : 'abcing'
'''

str = input("Enter a string: ")
if len(str) < 3:
    print(str)
else:
    if str[-3::] == "ing":
        print(str.replace("ing", "ly"))
    else:
        print(str + "ing")