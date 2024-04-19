l=[11,22,33,55,22,11,55,66,77,77,33,99,88,55,88]
newl=[]
for num in l:
    if num not in newl:
        newl.append(num)
print(newl)
