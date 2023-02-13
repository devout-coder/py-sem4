def sum_of_series(n):
    sum = 0
    for i in range(1, n+1):
        sum += 1/i
    return sum

n = 5
result = sum_of_series(n)
print("Sum of the series for n =", n, ":", result)