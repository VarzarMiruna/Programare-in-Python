#how many bits with value 1 a number has
def count_bits(number):
    count = 0
    while number:
        count = count + number % 2;
        number = int(number / 2)
    return count

print(count_bits(24)) #00011000
print(count_bits(240)) #11110000
print(count_bits(1298)) #10100010010