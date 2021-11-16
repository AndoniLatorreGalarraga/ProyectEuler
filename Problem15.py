def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

k = 20
n = k+1
print(factorial(n+k-1)/(factorial(k)*factorial(n-1)))
