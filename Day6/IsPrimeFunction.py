"""
判断一个数是不是素数
"""

def IsPrime(num):
    """判断一个数是不是素数"""
    for factor in range(2,num):
        if num % factor == 0:
            return False
    return True if num != 1 else False