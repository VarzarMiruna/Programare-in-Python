def find_primes(numbers):
    prime = []
    for i in range(len(numbers)):
        verify = 0
        for j in range(2, int(numbers[i] / 2) + 1):
            if numbers[i] % j == 0:
                verify = 1
                break
        if verify == 0:
            prime.append(numbers[i])
    return prime


numbers = [2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 23, 91]
print(find_primes(numbers))