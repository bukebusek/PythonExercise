"""
设计一个函数返回传入的列表中最大和第二大的元素的值

伪代码：
定义函数名,参数为列表
将列表位置0和位置1的值赋值给m1和m2
遍历列表 大于m1的赋值给m1，大于m2的赋值给m2，否则赋值
返回m1和m2

version:0.1
author:xukun
data:2021-03-10
"""

import random

def Max2(x):
    """

    :param x: 列表
    :return: 返回的最大值和第二大值
    """
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)): #index基本都需要-1 本次range自动-1 所以没有-1
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

if __name__ == '__main__':
    l1 = [1,2,3,4,5,19,7143,9710,95,7942,759,24,3]
    print(Max2(l1))