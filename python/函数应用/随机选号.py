import random

RED_BALLS = [i for i in range(1, 34)]
BLUE_BALLS = [i for i in range(1, 17)]

#生成一组随机号码
def choose():

    selected_balls = random.sample(RED_BALLS, 6)
    selected_balls.sort()
    selected_balls.append(random.choice(BLUE_BALLS))
    return selected_balls

# 格式输出一组号码
def display(balls):
    for ball in balls[:-1]:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    print(f'\033[034m{balls[-1]:0>2d}\033[0m')

n = int(input('生成几注号码: '))
for _ in range(n):
    display(choose())