def occurrences(x, *lis):
    ls = []
    for lis in lis:
        for el in lis:
            ls.append(el)
    res = []
    for el in ls:
        num = ls.count(el)
        if num == x:
            res.append(el)
    res = list(set(res))
    return res

#numerele care apar in liste de exact X ori

l1 = [1, 2, 3]
l2 = [2, 3, 4]
l3 = [4, 5, 6]
l4 = [4, 1, "test"]
x = 2

print(occurrences(x, l1, l2, l3, l4))