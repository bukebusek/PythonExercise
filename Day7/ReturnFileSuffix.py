"""
设计一个函数返回给定文件名的后缀名

伪代码：
找到文件名.的位置
如果.的位置在0-文件长度间
就返回.后面字符
通过参数判断返回是否需要带.
"""

def get_suffix(filename, has_dot=False):
    """
    :param filename: 文件名
    :param has_dot: 是否需要返回小数点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else  pos + 1
        return filename[index:]
    else:
        return '未找到后缀'

if __name__ == '__main__':
    filename = input('请输入完整文件名：')
    print(get_suffix(filename))