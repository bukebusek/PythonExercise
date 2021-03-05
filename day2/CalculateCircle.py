""""
输入半径计算圆的周长和面积
verson:0.1
author:xukun
"""

import math

redius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * redius
area = math.pi * (redius ** 2)
print('周长：%.2f'% perimeter )
print('面积：%.2f'% area)