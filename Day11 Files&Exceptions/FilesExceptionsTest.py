# -*- coding: utf-8 -*-
# @File    : FilesExceptionsTest.py
# @Author  : Xukun
# @Time    : 2021/4/1 01:34

def main():
    f = None
    try:
        f = open('致橡树。txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')
    finally:
        if f:
            f.close()

def main2():
    try:
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


import time


def main3():
    # 一次性读取整个文件内容
    with open('files/致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('files/致橡树.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('files/致橡树.txt') as f:
        lines = f.readlines()
    print(lines)

if __name__ == '__main__':
    main3()