def factorial(n):
    ''' returns n! '''
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(6))

fact = factorial

print(fact)

print(fact(5))

print(map(factorial, range(11)))

b = list(map(factorial, range(11)))
print(b)

b = dir(factorial)
print(b)

