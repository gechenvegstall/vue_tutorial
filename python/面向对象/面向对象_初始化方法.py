class Student:
    # 初始化
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')

    def play(self):
        print(f'{self.name}正在睡觉')

# 调用Student类的构造器创建对象并传入初始化参数
stu1 = Student('a', 1)
stu2 = Student('b', 1)
stu1.study('py')
stu2.play()