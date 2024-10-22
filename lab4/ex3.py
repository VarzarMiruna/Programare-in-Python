def compare(dict1, dict2):
    if type(dict1) != type(dict2):
        return False
    if type(dict1) != dict or type(dict2) != dict:
        if type(dict1) == set or type(dict1) == list:
            if len(dict1) != len(dict2):
                return False
            else:
                for i in range(len(dict1)):
                    if dict1[i] != dict2[i]:
                        return False
                return True
        else:
            if dict1 != dict2:
                return False
            return True
    if set(dict1.keys()) != set(dict2.keys()):
        return False
    for key in dict1:
        if not compare(dict1[key], dict2[key]):
            return False
    return True


dict1 = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': [1, 2, 3]}}
dict2 = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': [1, 2, 3]}}
print(compare(dict1, dict2))
dict3 = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': [1, 2, 4]}}
print(compare(dict1, dict3))