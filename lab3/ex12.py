def group_by_rhyme(lis):
    group = {}
    for word in lis:
        end = word[-2:]
        if end in group:
            group[end].append(word)
        else:
            group[end] = [word]
    final = list(group.values())
    return final


words = ['ana', 'banana', 'carte', 'arme', 'parte']
result = group_by_rhyme(words)
print(result)