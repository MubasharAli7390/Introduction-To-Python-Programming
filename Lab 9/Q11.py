#Remove an element from a if the wants to, else display the list as it is.
a = [1,2,3,4,5,6]
user_input = int(input("Enter 0 to remove an element form the list: "))
if user_input == 0:
    a.remove(2)
    print(a)
else:
    print(a)

