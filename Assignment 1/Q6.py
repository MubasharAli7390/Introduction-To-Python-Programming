'''Using the two strings: Skeleton Horseman

Make two new strings by swapping the first three letters of the first string with the last three letters of the second string

Make a single string from the two new strings

Print: The strings in their original order, The two new strings and the combined string

Expected output:
'''

string1 = "Skeleton" 
string2 = "Horseman"
new_str = string1.replace("Skel", "man")
combined_str = string1 + " " + string2
print("String 1: ", string1)
print("String 2: ", string2)
print("Swapped String: ", new_str)
print("Combined String", combined_str)