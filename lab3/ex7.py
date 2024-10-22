def palindrome(number):
    reverse = int(str(number)[::-1])
    if reverse == number:
        return True
    else:
        return False


def tup(ls):
    max_pal = 0
    nr = 0
    for x in ls:
        if palindrome(x):
            nr = nr + 1
            if x > max_pal:
                max_pal = x
    return nr, max_pal


ls = [121, 1, 23, 234, 1331, 2773]
no_of_pal, max_palindrome = tup(ls)
print("Number of palindromes: " + str(no_of_pal))
print("Greatest palindrome: " + str(max_palindrome))