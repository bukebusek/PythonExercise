"""
百分制成绩转换为等级制成绩

Version: 0.1
Author
"""

score = float(input('请输入成绩：'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else :
    grade = 'E'

print('学生的成绩是:%s' % grade)