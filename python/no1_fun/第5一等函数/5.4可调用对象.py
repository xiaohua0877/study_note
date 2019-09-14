# 用户定义的函数 使用 def 语句或 lambda 表达式创建。
# 内置函数使用 C 语言（CPython）实现的函数，如 len 或 time.strftime。
# 使用 yield 关键字的函数或方法。调用生成器函数返回的是生成器对象

b = abs, str, 13
print(b)

b = [callable(obj) for obj in (abs, str, 13)]
print(b)

#5.5用户定义的可调用类型