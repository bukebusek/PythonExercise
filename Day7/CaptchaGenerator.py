"""
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

伪代码：
定义函数名称
定义指定长度为参数
定义所需的随机字符
通过计算长度，定义每个字符的位置，for循环 通过随机选择位置，选择生成的字符
塞进密码里
返回结果

Version:0.1
Author:xukun
Data:2021-03-10
"""

import random

def Generator_code(code_len=4):
    """
    :param code_len:验证码的长度（默认4字符）
    :return:由大小写和数字构成的随机验证码
    """
    all_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

if __name__ == '__main__':
    print(Generator_code())