"""
输入两个正整数，计算他们的最大公约数和最小公倍数
version:0.1
author:xukun
date:2021-03-06
"""

x = int(input('x='))
y = int(input('y='))

if y > x:
    m,n = y,x
else:
    m,n = x,y
for z in range(1,n + 1):
    r = m % n #辗转相除法，使用辗转相除法：初始用a 模 b得到其余数，然后不断地用除数再去 模 余数，直到余数等于除数，所得的余数即为最大公约数
    if r == 0:
        print('%d和%d的最大公约数是%d' % (x,y,n))
        print('%d和%d的最小公倍数是%d' % (x,y,(x * y//n))) #最大公倍数：两数相乘除以最大公约数
        break
    else:
        m,n = n,r
