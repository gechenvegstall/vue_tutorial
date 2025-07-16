class Student:

    def study(self, course_name):
        print(f'学生正在学习{course_name}')

    def play(self):
        print(f'学生正在玩游戏')

stu1 = Student()
stu2 = Student()
print(stu1)
print(stu2)


Student.study(stu1, 'aaaaa')

stu1.study('A111')

Student.play(stu2)
stu2.play()