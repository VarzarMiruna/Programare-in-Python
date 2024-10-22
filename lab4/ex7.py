def set_operations(*sets):
    result = {}
    set_list = list(sets)
    for i in range(len(list(sets)) - 1):
        for j in range(i + 1, len(list(sets))):
            union = f"{set_list[i]} | {set_list[j]}"
            intersection = f"{set_list[i]} & {set_list[j]}"
            a_b = f"{set_list[i]} - {set_list[j]}"
            b_a = f"{set_list[j]} - {set_list[i]}"

            result[union] = set(set_list[i]).union(set(set_list[j]))
            result[intersection] = set(set_list[i]).intersection(set(set_list[j]))
            result[a_b] = set(set_list[i]).difference(set(set_list[j]))
            result[b_a] = set(set_list[j]).difference(set(set_list[i]))
    return result


a = {1, 2}
b = {2, 3}

res = set_operations(a, b)
print(res)