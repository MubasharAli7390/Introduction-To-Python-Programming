#Write a program to finding the position of a specific element in a list using the enumerate function and for loop with else in python.

list = [1,2,3,4,5,6,7,8,9,10]
for index, num in enumerate(list):
    if num == 5:
        print("index of five is:",index)
