# -*- coding: utf-8 -*- 
# @Time : 2021/4/1 7:25 下午 
# @Author : Xukun 
# @File : PygameTest6.py

import random
import pygame
import sys
from pygame.locals import *  #导入一些常用的函数

pygame.init()
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption('白黄大干') #定义窗口的标题为'乌龟吃鱼'
background = pygame.image.load("/Users/momo/Desktop/天安门.jpg").convert()
fishImg = pygame.image.load("/Users/momo/Desktop/白低于1.png").convert_alpha()
wuguiImg = pygame.image.load("/Users/momo/Desktop/白低于2.png").convert_alpha()

#乌龟吃掉小鱼的音乐  mp3格式的不行，wav格式的
#eatsound = pygame.mixer.Sound("C:\\Users\\Administrator\\Desktop\\achievement.wav")
#背景音乐
#pygame.mixer.music.load("C:\\Users\\Administrator\\Desktop\\game_music.mp3")
#pygame.mixer.music.play(loops=0, start=0.0)
#成绩文字显示
count=0
font =pygame.font.SysFont("arial", 40)
score = font.render("score %d"%count, True, (255, 255, 255))

w_width = wuguiImg.get_width()-5 #得到乌龟图片的宽度，后面留着吃鱼的时候用
w_height = wuguiImg.get_height()-5 #得到乌龟图片的高度

y_width = fishImg.get_width()-5 #得到鱼图片的宽度
y_height = fishImg.get_height()-5 #得到鱼图片的高度

fpsClock=pygame.time.Clock() #创建一个新的Clock对象，可以用来跟踪总共的时间
#乌龟类
class Turtle:
    def __init__(self):
        self.power=100 #体力
        #乌龟坐标
        self.x=random.randint(0,500)
        self.y=random.randint(0,400)
    #乌龟移动的方法：移动方向均随机 第四条
    def move(self,new_x,new_y):
        #判断移动后是否超出边界
        if new_x<0:
            self.x=0-new_x
        elif new_x>640:
            self.x=640-(new_x-640)
        else:
            #不越界则移动乌龟的位置
            self.x=new_x
        if new_y<0:
            self.y=0-new_y
        elif new_y>480:
            self.y=480-(new_y-480)
        else:
            #不越界则移动乌龟的位置
            self.y=new_y
        self.power-=1 #乌龟每移动一次，体力消耗1

    def eat(self):
        self.power+=20 #乌龟吃掉鱼，乌龟体力增加20
        if self.power>100:
            self.power=100 #乌龟体力100（上限）
#鱼类
class Fish:
    def __init__(self):
        #鱼坐标
        self.x=random.randint(0,500)
        self.y=random.randint(0,400)

    def move(self):
        new_x=self.x+random.choice([-10])
        if new_x<0:
            self.x=650
        else:
            self.x=new_x

#开始测试数据
tur=Turtle() #生成1只乌龟
fish=[] #生成10条鱼
for item in range(10):
    newfish=Fish()
    fish.append(newfish) #把生成的鱼放到鱼缸里

#pygame有一个事件循环，不断检查用户在做什么。事件循环中，如何让循环中断下来（pygame形成的窗口中右边的插号在未定义前是不起作用的）
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            #通过上下左右方向键控制乌龟的动向
            if event.key==pygame.K_LEFT:
                tur.move(tur.x-10,tur.y)
            if event.key==pygame.K_RIGHT:
                tur.move(tur.x+10,tur.y)
            if event.key==pygame.K_UP:
                tur.move(tur.x,tur.y-10)
            if event.key==pygame.K_DOWN:
                tur.move(tur.x,tur.y+10)

    screen.blit(background, (0, 0)) #绘制背景图片
    screen.blit(score,(500,20))#绘制分数
    #绘制鱼
    for item in fish:
        screen.blit(fishImg, (item.x, item.y))
        # pygame.time.delay(100)
        item.move() #鱼移动
    screen.blit(wuguiImg, (tur.x, tur.y)) #绘制乌龟
    #判断游戏是否结束：当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束
    if tur.power<0 or len(fish)==0:
        print("Game Over ~")
        sys.exit()
    for item in fish:
        # print("鱼",item.x,item.y,y_width,y_height)
        # print("乌龟",tur.x,tur.y,w_width,w_height)
        if ((tur.x < item.x + y_width) and (tur.x + w_width > item.x) and (tur.y < item.y + y_height) and (w_height + tur.y > item.y)) :
            tur.eat() #乌龟吃鱼的方法
            fish.remove(item) #鱼死掉
            #吃鱼音乐
            #eatsound.play()
            count=count+1 #累加
            score = font.render("score %d"%count, True, (255, 255, 255))
            print("死了一只鱼")
            print("乌龟最新体力值为 %d"%tur.power)

    pygame.display.update() #更新到游戏窗口
    fpsClock.tick(10) #通过每帧调用一次fpsClock.tick(10)，这个程序就永远不会以超过每秒10帧的速度运行