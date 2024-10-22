def count_characters(str):
    char_count = {}
    for char in str:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

#{'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .

string = "Ana has apples."
result = count_characters(string)
print(result)