"""
找出10000以内的完美数
完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。

伪代码:
通过取平方根
找出因子
再找出因子的对因子，并且因子与对因子并不相等
相加判断是否是完美数

Version:0.1
Author:xukun
Date:2021-03-07
"""

import math

for Num in range(1,10000):
    Result = 0
    for Factor in range(1,int(math.sqrt(Num)) + 1):
        if Num % Factor == 0:
            Result += Factor
            if Factor != 1 and Factor != Num // Factor:
                Result += Num // Factor
    if Result == Num:
        print(Num)


