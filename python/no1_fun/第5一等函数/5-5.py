def factorial(n):
    ''' returns n! '''
    return 1 if n < 2 else n * factorial(n - 1)


fact = factorial
b = list(map(fact, range(6)))
print(b)

b = [fact(n) for n in range(6)]
print(b)

b = list(map(factorial, filter(lambda n: n % 2, range(6))))
print(b)

b = filter(lambda n: n % 2, range(6))
print(b)


b = [factorial(n) for n in range(6) if n % 3]
print(b)
