#Capitalize the first letter of each word in a sentence using anonymous functions.
a = input("Enter a string: ")
r = ""
a_list = a.split()
result = list(map(lambda m: m.capitalize() ,a_list))
for i in result:
    r = r + i + " "
print (r)