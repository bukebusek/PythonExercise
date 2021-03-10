"""
计算指定的年月日是这一年的第几天

伪代码：

定义判断是不是闰年的函数
是返回True 不是返回False

定义输入的日期是这一年第几天的函数
参数为年 月 日

如果是闰年采用闰年计数
定义总天数
for循环月份 将对应的月份之前天数相加
返回之前的天数加本月到今天的天数
"""
import random

def is_leap_year(year):
    """

    :param year: 年份
    :return: True or False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year,month,date):
    """

    :param year: 年份
    :param month: 月份
    :param date: 日期
    :return: 返回总天数
    """
    days_of_month = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],\
                    [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]][is_leap_year(year)] # 如果是闰年是采用闰年计法
    totalday = 0 #变量不能在循环里定义
    for index in range(month - 1):
        totalday += days_of_month[index]
    return totalday + date

if __name__ == '__main__':
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))