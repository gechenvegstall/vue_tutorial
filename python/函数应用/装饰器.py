# def my_decorator(func):
#     def wrapper():
#         print("函数执行前")
#         func()  # 调用原始函数
#         print("函数执行后")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# # 调用被装饰后的函数
# say_hello()

# 带参数的
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("准备执行")
        result = func(*args, **kwargs)
        print("执行完")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(3, 4))