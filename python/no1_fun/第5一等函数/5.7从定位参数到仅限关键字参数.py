# Python 最好的特性之一是提供了极为灵活的参数处理机制，
# 而且 Python3 进一步提供了仅限关键字参数（keyword-only argument）。
# 与之密切相关的是，调用函数时使用 * 和 **“展开”可迭代对象，映射到单个参数。

def tag(name, *content, cls=None, **attrs):
    """生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

b =  tag('brtest')
print(b)
b = tag('p', 'hello')
print(b)

b =tag('p', 'hello', 'world')
print(b)

b = tag('p', 'hello', id=33)
print(b)

b = tag('p', 'hello', 'world', cls='sidebar')
print(b)
