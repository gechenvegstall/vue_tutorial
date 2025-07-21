# 定义一个三元组
t1 = (35, 12, 98)
# 定义一个四元组
t2 = ('aaa', 15, True, 'gd')
# 打包操作
a = 1, 10, 100
print(type(a))
print(a)
# 解包操作
i, j, k = a
print(i, j, k)
print(list(t2))
a=list(range(1,10))
print(tuple(a))
"""列表可变，元组不可"""