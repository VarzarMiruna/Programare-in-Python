print("UpperCamelCase into lowercase_with_underscores: ")
res = ""
initial = "MIRUNA"
for char in initial:
    if char.isupper():
        res = res + "_" + char.lower()
    else:
        res = res + char
if res[0] == '_':
    res = res[1:]
print(res)