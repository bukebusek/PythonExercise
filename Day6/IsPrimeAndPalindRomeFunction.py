"""
判断一个数是不是回文素数
"""

import IsPrimeFunction
import PalindromeFunction

if __name__ == '__main__':
    num = int(input('请输入正整数：'))
    if IsPrimeFunction.IsPrime(num) and PalindromeFunction.Is_Palindrome(num):
        print('%d是回文素数' % num)
    else:
        print('%d不是回文素数'% num)