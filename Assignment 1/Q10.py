'''Write a program that allows the user to enter a sentence then:

Count the number of characters in each word.

word is defined as a series of characters separated by a space

Print: the sentence, the longest word, the number of characters in the longest word'''

str = input("Enter a string: ")
a = str.split()
b_word = ""
for w in a:
    if len(w) > len(b_word):
        b_word = w
        
print("String: ",str)
print("longest word: ",b_word)
print("length of longest word: ",len(b_word))