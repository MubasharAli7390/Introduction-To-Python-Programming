#Filter out odd numbers from a list using anonymous functions.
series = [1,3,5,0,20,12,9]
result = list(filter (lambda m: m%2==0, series))
print(result)

