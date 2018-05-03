isDiv6= lambda n : True if n%2 == 0 and n%3 == 0 else False
print(isDiv6(12))
ls = [12,15,17,23,56,21,64,312]
print(list(filter(isDiv6,ls))
