"""
面向对象编程语言中，对象的属性通常会被设置为公开的（public），私有（private）或受保护（protected）的成员
__name表示一个私有属性，_name表示一个受保护属性
"""
# class Student:
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def study(self, course_name):
#         print(f'{self.__name}正在学习{course_name}.')
#
#
# stu = Student('a', 20)
# stu.study('Python程序设计')
# print(stu.__name)

"""动态属性"""
class Student:
    # __slots__ = ('name', 'age')
    # __slots__方法动态添加其他属性将会引发异常
    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('a', 20)
stu.sex = '男'

# 静态方法@staticmethod，类方法@classmethod
"""
实例方法：主要用于处理实例的状态，需要通过实例来调用。
类方法：主要用于操作类本身，比如创建类的实例、修改类属性等，可以通过类或实例调用。
静态方法：主要用于存放和类相关的工具函数，它和类的状态没有关系，同样可以通过类或实例调用。
"""
class MyClass:
    class_value = 20

    @classmethod
    def class_method(cls):
        return f"这是类方法，class_value 值为: {cls.class_value}"

# 直接通过类调用类方法
print(MyClass.class_method())
# 也可以通过实例调用类方法
obj = MyClass()
print(obj.class_method())

class MyClass:
    @staticmethod
    def static_method(a, b):
        return a + b

# 直接通过类调用静态方法
print(MyClass.static_method(3, 5))
