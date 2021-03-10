"""
打印杨辉三角

伪代码：
输入杨辉三角的行数
先定义杨辉为本行有多少空值
for循环确定行数
定义这一行有多少数字
包一for循环确定本行的每个位置的数字
只有第0位与最后1位为1
否则等于前一行本位+前一行的前一位相加
打印本行，结尾换行
"""

def yh_triangle_generator():
    num = int(input('请输入杨辉三角的行数：'))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1) #从0开始记所以要+1
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col],end='\t') #\t为制表符
        print() #折行

if __name__ == '__main__':
    yh_triangle_generator()