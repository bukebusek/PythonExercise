"""
工资结算系统
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成

输入abc模块的ABCMeta元类和abstractmethod
定义员工类 多态方法
初始化员工 设置参数
装饰器访问访问姓名
多态访问薪资

定义部门经理类 参数为姓名
初始化 继承姓名设置参数
定义月薪固定返回月薪 15000

定义程序员类 参数为姓名 工作时长09
初始化 继承姓名，设置参数
装饰器访问工作时长
装饰器设置工作时长 如果>0则为工作时长，否则为0
定义月薪 工作时长*150

定义销售员类 参数为姓名 销售额
初始化继承姓名 设置参数
装饰器访问销售额
装饰器设置销售额 如果>0则为销售额，否则为0
定义销售额 1200 + 0.05 * 销售额

定义主函数
输入员工列表
for循环员工列表
判断是否是程序员类 如果是 则输入工作时间
判断是否是销售员类 如果是 则输入销售额
打印本月工资
"""

from abc import ABCMeta, abstractmethod

class Employee(object, metaclass=ABCMeta):
    """员工"""
    def __init__(self, name):
        """
        初始化方法
        :param name:姓名 
        """
        self._name = name 
        
    @property
    def name(self):
        return self._name
    
    @abstractmethod
    def get_salary(self):
        """
        获得月薪
        :return:月薪 
        """
        pass
    
class Manager(Employee):
    """部门经理"""
    def __init__(self, name):
        super().__init__(name)
    
    def get_salary(self):
        return 15000.00
    
class Programmer(Employee):
    """程序员"""
    def __init__(self, name, working_hour=0):
        super(Programmer, self).__init__(name)
        self._working_hour = working_hour
    
    @property
    def working_hour(self):
        return  self._working_hour
    
    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0
    
    def get_salary(self):
        return 150.00 * self._working_hour
    
class Salesman(Employee):
    """销售员"""
    
    def __init__(self, name, sales=0):
        super(Salesman, self).__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200.00 + self._sales * 0.05

def main():
    emps = [
        Manager('刘备'), Programmer('诸葛亮', 80),
        Manager('曹操'), Salesman('荀彧', 20000),
        Salesman('吕布'), Programmer('张辽', 120),
        Programmer('赵云', 50)
    ]
    for emp in emps:
        #if isinstance(emp, Programmer):
            #emp.working_hour = int(input('请输入%s本月的工作时间' % emp.name))
        #elif isinstance(emp, Salesman):
            #emp.sales = float(input('请输入%s本月的销售额' % emp.name))
        print('%s本月工资为：￥%s元' % (emp.name, emp.get_salary()))

if __name__ == '__main__':
    main()

