# -*- coding: utf-8 -*- 
# @Time : 2021/3/31 7:30 下午 
# @Author : Xukun 
# @File : TinkerTest2.py

from tkinter import *


class Application(Frame):
    def __init__(self, master=None):#每个Button、Label、输入框等，都是一个Widget
        Frame.__init__(self, master) #Frame是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
        self.pack()#pack方法把Widget加入到父容器中，并实现布局，grid()可以实现更复杂的布局
        self.createWidgets()#abel和一个Button，当Button被点击时，触发self.quit()使程序退出

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()