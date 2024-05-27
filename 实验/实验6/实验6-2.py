# 引入随机库
import random
# 定义一个矩形类
class rectangle():
    # 类属性：用于计算对象的创建个数
    count=0
    # 构造方法
    def __init__(self,alpha,beta):
        # 实例属性：长，宽
        self.alpha,self.beta=alpha,beta
        # 每构造一次sum+1
        rectangle.count+=1
    # 实例方法：计算周长
    def Girth(self):
        return 2*(self.alpha+self.beta)
    # 实例方法：计算面积
    def Area(self):
        return self.alpha*self.beta
    # 实例方法输出周长和面积
    def Print_Grith_Area(self):
        print(f"周长为{self.Girth()}，面积为{self.Area()}")
    # 类方法：根据给定的周长和面积，返回一个矩形对象
    @classmethod
    def class_method(cls,Girth,Area):
        Alpha=Girth/4-((Girth/4)**2-Area)**(1/2)
        Beta=Girth/4+((Girth/4)**2-Area)**(1/2)
        # 返回一个矩形对象
        return cls(Alpha,Beta)
# 生成一个随机数n（n在100到999之间）
n=random.randint(100,999)
# 生成n个长宽（都为整数）都在[10,20]之间的矩形对象
for i in range(n):
    rectangle(random.randint(10,20),random.randint(10,20))
# 类方法生成两个矩形（一个矩形周长为14，面积为12，另一个矩形周长为30，面积为56）对象
rectangle.class_method(14,12)
rectangle.class_method(30,56)
# 输出程序共生成的矩形总数
print(f"程序共生成的矩形总数为{rectangle.count}")