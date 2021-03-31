# -*- coding: utf-8 -*-
# @File    : CopyFiles.py
# @Author  : Xukun
# @Time    : 2021/4/1 02:30

def main():
    try:
        with open('files/mm.jpg', 'rb') as f1:
            data = f1.read()
            print(type(data))
        with open('files/梅梅.jpg', 'wb') as f2:
            f2.write(data)
    except FileNotFoundError as e :
        print('指定的文件无法打开')
    except IOError as e:
        print('读写文件时出现错误')
    print('程序执行结束')

if __name__ == '__main__':
    main()