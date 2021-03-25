"""
奥特曼打小怪兽

定义战斗者类 绑定姓名和生命 定义是否活着 攻击为多态
定义奥特曼类 绑定初始初始化 姓名 生命 魔法 多态普通攻击 定义的大招 魔法攻击 和恢复魔法值 定义返回的名称 定义随机选择技能的函数
定义怪兽类 绑定初始化姓名 生命 定义攻击 定义返回的姓名
定义判断是否有活着的怪兽 定义随机选一只怪兽 定义显示信息
定义主函数 定义奥特曼和怪兽的信息 定义战斗回合数
当奥特曼和怪兽都活着则继续战斗 打印战斗回合数
奥特曼攻击 如果小怪兽活着则反击
打印本轮回合结束的信息
打印回合接受 结束循环则打印战斗结束 谁赢的信息
"""

from abc import ABCMeta, abstractmethod
from random import randint, randrange, sample
import time

class Fighter(object, metaclass=ABCMeta):
    """战斗者"""
    __slots__ = ('_name', '_hp')
    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def normal_attack(self, other):
        """
        普通攻击
        """
        pass

class Ultraman(Fighter):
    """奥特曼"""

    __slots__ = ('_name', '_hp', '_mp')
    def __init__(self, name, hp , mp):
        super(Ultraman, self).__init__(name, hp)
        self._mp = mp

    def normal_attack(self, other):
        injury = randint(15, 25)
        other.hp -= injury
        print('%s奥特曼使用了普通攻击打了%s,%s掉了%s血\n' % (self._name, other.name, other.name, injury))

    def huge_attack(self, other):
        """
        大招
        :param other: 被攻击对象
        :return: 成功返回True不成功返回False
        """
        print('%s准备使用大招！' % self._name)
        if self._mp >= 0:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            print('%s奥特曼使用了大招虐暴打了%s,%s掉了%s血\n' % (self._name, other.name, other.name, injury))
            return True
        else:
            print('%s奥特曼能量不足！只能使用普通攻击\n' % (self._name))
            self.normal_attack(other)
            return False

    def magic_attack(self, other):
        """
        魔法攻击
        :param other: 被攻击对象
        :return: 成功返回True，否则返回False
        """
        print('%s奥特曼准备使用魔法攻击！\n' % self._name)
        if self._mp >= 20:
            self._mp -= 20
            injury = randint(10, 20)
            other.hp -= injury
            list = ['电刑', '火烧', '水淹', '刀刮']
            injury_type = ''.join(sample(list, 1))
            print('%s奥特曼使用了%s攻击了%s,%s掉了%s血\n' % (self._name, injury_type, other.name, other.name, injury))
            return True
        else:
            print('%s奥特曼能量不足！无法攻击\n' % self._name)
            return False

    def resume(self):
        """恢复魔法值"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        print('%s奥特曼恢复了魔法值%s点\n' % (self._name, incr_point))
        return incr_point


    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
               '生命值：%d\n' % self._hp + \
               '魔法值：%d\n' % self._mp

class Monster(Fighter):
    """打妖怪"""
    __slots__ = ('_name', '_hp')
    def __init__(self, name, hp):
        super(Monster, self).__init__(name, hp)

    def normal_attack(self, other):
        injury = randint(1, 10)
        other.hp -= injury
        print('大妖怪%s居然反击了%s,%s掉了%s血\n' % (self._name, other.name, other.name, injury))

    def __str__(self):
        return '~~~%s大妖怪~~~\n' % self._name + \
               '生命值: %d\n' % self._hp

def is_any_alive(monsters):
    """判断有没有小怪兽活着"""
    for monster in monsters:
        if monster.alive > 0:
            return True
        else:
            return False

def select_alive_one(monsters):
    """选中一只活着的小怪兽"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def display_info(ultraman, monsters):
    """显示奥特曼和小怪兽的信息"""
    print("---------奥特曼和大妖怪们的状态--------\n")
    print(ultraman)
    time.sleep(1)
    for monster in monsters:
        print(monster)
        time.sleep(1)

def main():
    u = Ultraman('徐堃', 200, 100)
    m1 = Monster('董国舅', 100)
    m2 = Monster('苗儿', 75)
    m3 = Monster('小熊', 50)
    ms = [m1, m2, m3]
    fight_round = 1
    print('========战斗开始========')
    time.sleep(1)
    while u.alive > 0 and is_any_alive(ms):
        print('========第%02d回合========' % fight_round)
        m = select_alive_one(ms)
        skill = randint(1, 10)
        if skill <= 6:
            u.normal_attack(m)
            u.resume()
        elif skill <= 9 :
            u.magic_attack(m)
        else:
            u.huge_attack(m)

        if m.alive > 0 :
            m.normal_attack(u)

        time.sleep(2)

        display_info(u, ms)

        fight_round += 1


    print('\n========战斗结束!========\n')

    if u.alive > 0:
        print('%s奥特曼光荣胜利了！' % u.name)
    else:
        print('大妖怪们居然赢了！')

if __name__ == '__main__':
    main()



