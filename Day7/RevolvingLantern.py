
"""
滚动显示走马灯上的文字

伪代码：
定义内容
清屏
打印内容
休眠0.2s
修改内容，首字符至末尾
循环

Version:0.1
Autehor:xukun
Data:2020-03-10
"""

import os
import time

def main():
    content = '     我一路向北，離開有你的季節，你說你好累，已無法再愛上誰    '
    while True:
        os.system('clear') #清屏命令
        print(content)
        time.sleep(0.2) #休眠0.2s
        content = content[1:]+content[0]

if __name__ == '__main__':
    main()
