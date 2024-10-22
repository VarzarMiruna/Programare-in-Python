def find_words(string):
    nr = 0
    for ch in string:
        if ch == ' ':
            nr = nr + 1
    nr = nr + 1
    return nr

print(find_words("I have Python exam"))

print(find_words("Python"))

print(find_words("Python "))