def filtering(x=1, strings=[], flag=True):
    lis = []
    for string in strings:
        chars = []
        for char in string:
            if flag:
                if ord(char) % x == 0:
                    chars.append(char)
            else:
                if ord(char) % x != 0:
                    chars.append(char)
        lis.append(chars)
    return lis

#afiseaza literele la care codul ascii  nu e divizibil cu nr meu X
x = 2
strings = ["test", "hello", "lab002"]
flag = False #care sa nu fie
res = filtering(x, strings, flag)
print("Literele care NU sunt divizibile cu", x)
print(res)

x = 2
strings = ["test", "hello", "lab002"]
flag = True
res = filtering(x, strings, flag)
print("Literele care sunt divizibile cu", x)
print(res)

#t=84, e=69, s=83, h=72, l=76, o=79, a=65, b=66