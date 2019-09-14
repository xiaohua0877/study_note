import random


class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        print(self._items)
        random.shuffle(self._items)
        print(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(10))
b = bingo.pick()
print(b)

b = bingo()
print(b)

b = callable(bingo)
print(b)

# 5.7从定位参数到仅限关键字参数