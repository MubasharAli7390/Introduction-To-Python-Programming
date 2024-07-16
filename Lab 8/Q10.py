#Calculate the sum of variable-length numbers using *args arguments.
def sum(*abc):
    sum = 0
    for i in abc:
        sum = sum + i
    return sum

print("sum: ",sum(2,5,8))
