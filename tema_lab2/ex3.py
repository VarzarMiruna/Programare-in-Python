#receives two strings and prints the number of occurrences of the first string in the second

string1 = input("Introduce the first string: ")
string2 = input("Introduce the second string: ")
nr = 0
initialIndex = 0
pos = 0
if len(string1) > len(string2):
    print("There are 0 occurrences of string1 in string2.")
else:
    while initialIndex < len(string2):
        pos = string2.find(string1, initialIndex)
        if pos != -1:
            nr = nr + 1
            initialIndex = pos + 1
        else:
            initialIndex = len(string2)
    print("There are " + str(nr) + " occurrences of string1 in string2.")