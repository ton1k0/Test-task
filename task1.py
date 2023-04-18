import math

def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def func(n, m):
    numbers = list(range(1, n + 1))
    length = len(numbers)
    number_of_variants = 2 ** (n - 1)

    for i in range(1, number_of_variants):
        expression = ''
        for j in range(length):
            expression += str(numbers[j])
            if j < length - 1 and (i & (1 << j)) > 0:
                expression += '+'

        sum = eval(expression)

        if sum == m:
            return f"{expression}={sum}"

print(func(5, 15))
print(func(4, 127))

