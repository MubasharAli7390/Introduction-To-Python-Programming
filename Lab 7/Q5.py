#reverse a list a list in python using a function
def rev(a):
    re_s = ''
    s_list = list(a)
    length = len(s_list)
    i = length
    while i > 0:
        re_s = re_s + a[i-1]
        i = i - 1
    return re_s
s = "mubashar"
print("reverse sting:",rev(s))

