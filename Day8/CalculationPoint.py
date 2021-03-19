"""
定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法

定义类
初始化
定义移动至固定位置函数
定义移动置顶增量函数
定义计算与另一指定点距离的函数
"""

from math import sqrt

class Point(object):
    def __init__(self, x=0, y=0):
        """
        :param x: 横坐标
        :param y:纵坐标
        """
        self.x = x
        self.y = y

    def MoveTo(self, x, y):
        """

        :param x:新的横坐标
        :param y:新的纵坐标
        """
        self.x = x
        self.y = y

    def MoveBy(self, dx, dy):
        """

        :param dx: 横坐标增量
        :param dy: 纵坐标增量
        :return:
        """
        self.x += dx
        self.y += dy

    def DistanceTo(self, other):
        """
        计算与另一个点的距离
        :param other: 另一个点
        :return:返回距离
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s,%s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    p1.MoveTo(7, 8)
    print(p1)
    print(p2)
    p2.MoveBy(-1, 2)
    print(p2)
    print(p1.DistanceTo(p2))

if __name__ == '__main__':
    main()