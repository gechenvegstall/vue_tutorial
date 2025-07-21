# dict函数(构造器)中的每一组参数就是字典中的一组键值对
person = dict(name='xiaoc', age=15, height=188, weight=60, addr='广东省')
print(person)

# 可以通过Python内置函数zip压缩两个序列并创建字典
items1 = dict(zip('ABCDE', '12345'))
print(items1)