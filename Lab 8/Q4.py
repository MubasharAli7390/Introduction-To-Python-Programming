#Double each element in a list using anonymous functions.
series = [1,3,5,0,20,12,9]
result = list(map (lambda m: m+m, series))
print("doubled list:",result)


