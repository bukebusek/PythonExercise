"""
定义一个描述数字时钟

伪代码：
初始化，定义小时 分钟 秒
定义走表
定义时间展示
主执行函数
"""

from time import sleep
import os

class Clock(object):

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.secoud = second

    def run(self):
        """
        走字
        """
        self.secoud += 1
        if self.secoud == 60:
            self.secoud = 0
            self.minute += 1
            if self.minute == 60:
                self.hour += 1
                self.minute = 0
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        return '%02d:%02d:%02d' % \
               (self.hour, self.minute, self.secoud)

def main():
    clock = Clock(23, 59, 59)
    while True:
        print(clock.show())
        sleep(1)
        os.system('clear')
        clock.run()

if __name__ == '__main__':
        main()