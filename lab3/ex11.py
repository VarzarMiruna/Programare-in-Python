def keys(e):
    return e[1]

def sort(lis):
    list_to_ord = [0] * len(lis)
    pos = 0
    new_list = []
    for tup in lis:
        if len(tup) < 2:
            list_to_ord[pos] = ord('a') - 1
        else:
            if len(tup[1]) < 3:
                list_to_ord[pos] = ord('a') - 1
            else:
                list_to_ord[pos] = ord(tup[1][2])
        new_list.append((tup, list_to_ord[pos]))
        pos = pos + 1

    new_list.sort(key=keys)
    final_list = []
    for tup in new_list:
        final_list.append(tup[0])
    return final_list

#[(('abc', 'bcd'), 100), (('abc', 'zza'), 97)]

input_list1 = [('abc', 'bcd'), ('abc', 'zza'), ('add', 'bbb')] #d=100 a=97 b=98
input_list2 = [('abc', 'bcd'), ('abc', 'zza')] #d=100 a=97
print(sort(input_list1))
print(sort(input_list2))