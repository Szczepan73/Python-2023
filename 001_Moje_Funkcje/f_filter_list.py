def filter_list(l):
    lst2 = []
    for y in range(0, len(l)):
        if type(l[y]) == type(1):
            lst2.append(l[y])
    return lst2
