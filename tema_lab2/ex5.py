def palindrome(number):
    reverse = int(str(number)[::-1])
    if reverse == number:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")

palindrome(1001)
palindrome(122221)
palindrome(2004002)

palindrome(1090)
palindrome(10870)
palindrome(10340)