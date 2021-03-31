# -*- coding: utf-8 -*-
# @File    : JsonTest.py
# @Author  : Xukun
# @Time    : 2021/4/1 02:46

import json

def main():
    mydict = {
        'name': '徐堃',
        'age': 27,
        'qq': 779742678,
        'friends': ['董丕龙', '苗小壮'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('files/json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('数据保存完成')

if __name__ == '__main__':
    main()