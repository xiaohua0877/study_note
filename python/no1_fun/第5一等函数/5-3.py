fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'bss']
fruits1 = ['strawberry', 'fig', 'appl e ', 'cherry', 'raspberry', 'bss']

b = sorted(fruits, key=len)
print(b)


def reverse(word):
    return word[::-1]


b = reverse('testint dji code')
print(b)

b = sorted(fruits, key=reverse)
print(b)

b = sorted(fruits1, key=reverse)
print(b)