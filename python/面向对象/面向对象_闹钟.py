import time
# 定义时钟类
class Clock:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.min = minute
        self.sec = second

    def run(self):
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0
    # 时间显示
    def show(self):
        return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'


# 创建时钟对象
clock = Clock(00, 0, 0)
while True:
    print(clock.show())
    time.sleep(1)
    clock.run()