# 参数1元组，2字典
def calc(*args, **kwargs):
    total = sum(args)
    # 处理关键字参数
    if 'scale' in kwargs:
        total *= kwargs['scale']
    if 'offset' in kwargs:
        total += kwargs['offset']

    return total
result1 = calc(1, 2, 3)
print(result1)
result2 = calc(1, 2, 3, scale=2)
print(result2)

'''
lambad函数,称匿名函数。lambda 函数是没有的名字函数
lambda 参数列表: 表达式（参数列表：多个参数用逗号分隔（如 x, y），表达式：函数的返回值（只能有一个表达式，不能包含语句或代码块））
'''
# 普通函数
def add(x, y):
    return x + y

# lambda 函数
add_lambda = lambda x, y: x + y

print(add(3,5))
print(add_lambda(3,5))