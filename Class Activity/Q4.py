#Define a user defined function to check if year is a leap year
yr = int(input("Enter a number: "))
def leap_year(y):
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        return "Year is a leap year"
    else:
        return "Year is not a leap year"
print(leap_year(yr))
