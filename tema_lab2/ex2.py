#how many vowels are in a string
string = input("Write a string: ")
nr = 0
vowels = "aeiouAEIOU"
for i in range(len(string)):
    if string[i] in vowels:
        nr = nr + 1
print("The number of vowels in " + string + " is " + str(nr))