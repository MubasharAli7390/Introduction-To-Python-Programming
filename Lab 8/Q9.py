#Filter a list of strings to include only those starting with a specific letter.
li = ['Ali','Mubashar','Car','Random','number']
filtered_list = list(filter(lambda a: a[0] == 'C' ,li))
print(filtered_list)
