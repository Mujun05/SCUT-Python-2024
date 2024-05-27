# 定义一个三角形类
class triangle():
    # 三个实例属性（三个边长）
    def __init__(self,alpha,beta,gamma):
        self.alpha,self.beta,self.gamma=alpha,beta,gamma
    # 编写两个实例方法，分别计算周长和面积
    def Girth(self):
        return self.alpha+self.beta+self.gamma
    def Area(self):
        p=(self.alpha+self.beta+self.gamma)/2
        return (p*(p-self.alpha)*(p-self.beta)*(p-self.gamma))**(1/2)
# 创建一个边长分别为3，4，5的三角形对象
tri=triangle(3,4,5)
# 输出它的周长和面积
print(f"边长分别为3，4，5的三角形的周长为{tri.Girth()}，面积为{tri.Area()}")