#check if a string in palidrome or not using python function
def palidrome(w):
    re_s = ''
    s_list = list(w)
    length = len(s_list)
    i = length
    while i > 0:
        re_s = re_s + w[i-1]
        i = i - 1
    if re_s == w:
        return "The given string is a palidrome"
    else:
        return "The given string is not a palidrome"
    
s = "racecar"
print(palidrome(s))



