"""
约瑟夫环问题

幸运的基督徒
有15个基督徒和15个非基督徒在海上遇险，
为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，
由某个人开始从1报数，报到9的人就扔到海里面，
他后面的人接着从1开始报数，
报到9的人继续扔到海里面，直到扔掉15个人。
由于上帝的保佑，15个基督徒都幸免于难，
问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。

伪代码：
初始设置，所有人状态均为True，count index num均为 0
计数到15则停止循环
数数index num同时+1 index大于30则要取余数
数到9则状态由True改变至False，num归0 count +1
输出结果 True为基督徒，False为非基督徒

"""

def main():
    persons = [True] * 30
    counter, index, num = 0, 0, 0
    while counter < 15:
        if persons[index] :
            num += 1
            if num == 9:
                persons[index] = False
                num = 0
                counter += 1
        index += 1
        index %= 30
    x = []
    for person in persons :
        x.append('基'if person else '非')
    for i, y in enumerate(x):
        print(i, y)
    #print(list(enumerate(x)))

if __name__ == '__main__':
    main()
