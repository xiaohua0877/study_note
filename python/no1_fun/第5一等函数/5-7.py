# lambda 关键字在 Python 表达式内创建匿名函数
# 示例 5-7 使用 lambda 表达式反转拼写，然后依此给单词列表排序
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
b = sorted(fruits, key=lambda word: word[::-1])
print(b)

# 5.4可调用对象