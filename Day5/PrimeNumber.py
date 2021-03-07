"""
输出100以内所有的素数

素数指的是只能被1和自身整除的正整数（不包括1）
伪代码：

100for循环
判断是否是素数
是的话打印


Version:0.1
Author:xukun
Date:2021-03-07
"""


import math

for a in range(2, 100):
    IsPrime = True
    for b in range(2, int(math.sqrt(a)) + 1): #决定不能有1！
        if a % b == 0:
            IsPrime = False
            break
    if IsPrime:
        print(a, end=' ')
