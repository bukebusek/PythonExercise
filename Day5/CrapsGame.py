"""
Craps赌博游戏
该游戏使用两粒骰子
玩家第一次摇骰子如果摇出了7点或11点，玩家胜
玩家第一次如果摇出2点、3点或12点，庄家胜
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜
如果玩家摇出了第一次摇的点数，玩家胜
其他点数，玩家继续要骰子，直到分出胜负

伪代码：
设定玩家开始有1000注
游戏结束条件是玩家输光所有赌注
下注过程
判断下注是否大于0小于所有金额
如果不是则提示用户从新下注
成功下注则开始要骰子
第一次摇骰子 如果摇出了7点或11点，玩家胜 如果摇出2点、3点或12点，庄家胜
其他点数玩家继续摇骰子 如果玩家摇出了7点，庄家胜 如果玩家摇出了第一次摇的点数，玩家胜
其他点数，玩家继续要骰子，直到分出胜负

version:0.1
Author:xukun
Data:2021-03-06
"""

from random import randint

Money = 1000
while Money >0:
    print('你的总资产为%s：' % Money)
    while True:
        Debt = int(input('请下注：'))
        if 0 < Debt <= Money:
            print('你本次的注资为%s' % Debt)
            break
        else:
            print('请重新下注！')
    FirstTime = randint(1,6) + randint(1,6)
    print('你摇出了：%d' % FirstTime )
    if FirstTime == 7 or FirstTime == 11:
        print('你赢了！')
        Money += Debt
    elif FirstTime == 2 or FirstTime == 3 or FirstTime ==12:
        print('庄家赢了')
        Money -= Debt
    else:
        NeedsGoOn = True
    while NeedsGoOn:
        NeedsGoOn = False
        OtherTime = randint(1,6) + randint(1,6)
        print('你摇出了：%d' % OtherTime)
        if OtherTime == 7:
            print('庄家赢了')
            Money -= Debt
        elif OtherTime == FirstTime:
            print('你赢了')
            Money +=Debt
        else:
            NeedsGoOn = True
print('你破产了，游戏结束！')

