"""
判断年份是不是闰年
verson:0.1
author:xukun
"""

year = int(input('请输入年份：'))
is_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(is_year)