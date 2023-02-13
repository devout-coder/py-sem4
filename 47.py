def sum_of_series(x, n):
    sum = 0
    for i in range(1, n+1):
        sum += x**i/i
    return sum

x = 2
n = 5
result = sum_of_series(x, n)
print("Sum of the series for x =", x, "and n =", n, ":", result)
