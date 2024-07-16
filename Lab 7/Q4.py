#find the number of vowels in a list using a function
def vow(a):
    n = 0
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for i in a:
        for j in vowels:
            if i == j:
                n += 1
    return n

li = ['M','u','b','a','s','h','a','r']
print("number of vowels:",vow(li))