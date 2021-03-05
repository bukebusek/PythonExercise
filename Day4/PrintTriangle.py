"""
打印三角形图案
version:0.1
author:xukun
"""

row = int(input('请输入行数：'))

for i in range(row): #控制行数
    for _ in range(i + 1):
        print('*',end='')
    print() #这个print控制着换行，for函数会默认换行
print()

for i in range(row): #range（5）的范围为（0~4）
    for j in range(row):
        if j < row - i - 1:
            print(' ',end='')
        else:
            print('*',end='')
    print()
print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ',end='')
    for _ in range(2 * i + 1):
        print('*',end='')
    print()