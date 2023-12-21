lst = []
lst.append(2)
x
print(lst)
lst2 = []
for y in range(0, len(lst)):
    if type(lst[y]) == type(1):
        lst2.append(lst[y])
print (lst)
print(lst2)
