"""
双色球选号

规则：红球一共6组，每组从1-33中抽取一个，六个互相不重复。然后蓝球是从1-16中抽取一个数字，这整个组成的双色球

伪代码：
规定红球的数字范围
规定选择的球为一个数组
红球选择：从中选择不重复的6个元素，并排序
蓝球选择：从1-16中抽取一个数字，添加至数组中
返回所选选择的球的结果

展示结果：
展示蓝球前增加|
展示两位整数

整体函数：
输入机选几注
for循环展示结果
"""

from random import randrange, randint, sample

def random_select():
    """
    :return: 返回选择的号码的数组
    """
    red_ball = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_ball, 6) #sample函数来实现从列表中选择不重复的n个元素
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls

def display(balls):
    """
    :param balls: 选择的球的号码列表
    :return: 输出列表中的双色球号码
    """
    for index, ball in enumerate(balls): #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
        if index == len(balls) - 1:
            print('|', end=' ') #红篮球用竖线分割
        print('%02d' % ball, end=' ')
    print() #折行

def main():
    n = int(input('请输入机选几注：'))
    for _ in range(n):
        display(random_select())

if __name__ == '__main__':
    main()