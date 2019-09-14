from functools import reduce
from operator import add
b = reduce(add, range(10))
print(b)

b = sum(range(10))
print(b)

b = all(iter)
print(b)