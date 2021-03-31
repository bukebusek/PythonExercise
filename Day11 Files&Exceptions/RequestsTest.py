# -*- coding: utf-8 -*-
# @File    : RequestsTest.py
# @Author  : Xukun
# @Time    : 2021/4/1 02:54

import requests
import json


def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()