"""
Craps赌博游戏
该游戏使用两粒骰子
玩家第一次摇骰子如果摇出了7点或11点，玩家胜
玩家第一次如果摇出2点、3点或12点，庄家胜
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜
如果玩家摇出了第一次摇的点数，玩家胜
其他点数，玩家继续要骰子，直到分出胜负

我们设定玩家开始有1000注
游戏结束条件是玩家输光所有赌注

version:0.1
Author:xukun
Data:2021-03-06
"""

from random import randint
