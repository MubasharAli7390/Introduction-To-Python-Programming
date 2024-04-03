#Checking if a year is a century year (ending in 00).

year = str(input("Enter the year: "))
year_end = year[2:4]
if year_end == "00":
    print("The year is a century")
else:
    print("The year is not a century")