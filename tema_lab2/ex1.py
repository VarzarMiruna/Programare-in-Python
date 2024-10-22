#1. Find The greatest common divisor of multiple numbers read from the console.
def gcdF(a, b):
    while (a < 0 and b < 0):
        if (a > b):
            b = b % a
        else:
            a = a % b

    while (a > 0 and b > 0):
        if (a > b):
            a = a % b
        else:
            b = b % a

    if (a == 0):
        return b
    return a

def gcdArrarray(arr):
    g = 0
    for i in range(len(arr)):
        g = gcdF(g, arr[i])
    return g

print("Minimum 2 numbers, write 'gata' for exit and result")
value = input("Number: ")
n = 0
numbers = [0]
while 1:
    try:
        num = int(value)
        numbers.append(0)
        numbers[n] = num
        n = n + 1
        value = input("Number: ")

    except ValueError:
        if not isinstance(value, int):
            print("GATA :D.")
            break

if len(numbers) < 2:
    print("You introduced to few numbers.")
else:
    res = numbers[0]
    for numb in numbers[1:len(numbers) - 1]:
        res = gcdF(res, numb)
    print("The greatest common divisor is: " + str(res))

