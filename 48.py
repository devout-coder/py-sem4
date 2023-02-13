import math

def calculate_euler(n):
    e = 0
    for i in range(0, n+1):
        e += 1/math.factorial(i)
    return e

n = 10
euler = calculate_euler(n)
print("Euler's number with", n, "iterations:", euler)