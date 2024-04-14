#Checking if a given year is in the past, present, or future
year = int(input("Enter the year: "))
if year == 2024:
    print("It is the present year")
elif year > 2024:
    print("The year is in the future")
else:
    print("The year is in the past")