from django.db.models import Avg, Count, Sum
from django.shortcuts import render,HttpResponse

from .models import Student,Score,Course,Teacher

def read_user(request):
    # 查询平均成绩大于60分的同学的id和平均成绩
    # rows =Student.objects.annotate(avg=Avg("score__number")).filter(avg__gte=60).values("id", "avg")
    # for row in rows:
    #     print(row)

    # 查询所有同学的id、姓名、选课的数、总成绩
    # rows =Student.objects.annotate(course_nums=Count("score__course"), total_score=Sum("score__number")).values("id", "name", "course_nums", "total_score")
    # for row in rows:
    #     print(row)

    # 查询所有课程成绩小于60分的同学的id和姓名
    # students = Student.objects.exclude(score__number__gt=60)
    # for student in students:
    #     print(student)

    # 查询每门课程的平均成绩，按照平均成绩进行排序
    # courses =Course.objects.annotate(avg=Avg("score__number")).order_by('avg').values('id', 'name', 'avg')
    # for course in courses:
    #     print(course)

    # 查询两门以上不及格的同学的id、姓名、以及不及格课程数
    # students =Student.objects.annotate(bad_count=Count("score__number", filter=Q(score__number__lt = 60))).filter(bad_count__gte=2).values('id', 'name', 'bad_count')
    # for student in students:
    #     print(student)
    return HttpResponse('查询成功')

