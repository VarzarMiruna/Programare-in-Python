def fibo(n):
    f1 = 0
    f2 = 1
    numbers = [0] * n;
    if n == 0:
        return numbers
    else:
        numbers[0] = f1;
        if n == 1:
            return numbers
        else:
            numbers[1] = f2;
            i = 2
            if n == 2:
                return numbers
            else:
                while i < n:
                    f3 = f1 + f2
                    numbers[i] = f3
                    f1 = f2
                    f2 = f3
                    i = i + 1
                return numbers


print(fibo(7))