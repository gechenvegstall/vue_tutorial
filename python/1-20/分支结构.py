# height=float(input("身高(cm)："))
# weight=float(input("体重(kg)："))
# bmi=weight/(height/100)**2
# print(f"{bmi=:.1f}")
# if 18.5<=bmi<24:
#     print("good")
# elif bmi<30:
#     print("一般般")
# else:
#     print("差点")

"""match-case"""
# code=int(input("响应码："))
# match code:
#     case 200:print("ok")
#     case 400:print("a")
#     case _:print("no")

"""循环"""
# a=int(input("请输入数字："))#range生成1-n的数
# for a1 in range(1,a):
#     print(a1)

num=0
while num<100:
    print(f"当前为数字：{num}")
    num+=1
else:
    print("结束+")