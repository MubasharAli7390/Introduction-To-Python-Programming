'''Using the string from the previous exercise
Create and print a substring comprising first and last characters

Create and print a substring comprising the first two characters and the last two characters

Create and print a substring comprising the letters after the character t and before the second character a'''

string = "Minecraft is Awesome"
#Create and print a substring comprising first and last characters
first1 = string[0]
last1 = string[-1]
print("first and last: ", first1 + last1)
#Create and print a substring comprising the first two characters and the last two characters
first2 = string[0:2]
last2 = string[-2:]
print("first two and last two: ", first2 + last2)
#Create and print a substring comprising the letters after the character t and before the second character a
letters = string[9:13]
print("before T and second char A: ",letters)