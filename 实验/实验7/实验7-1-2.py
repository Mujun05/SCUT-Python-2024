# 定义三角形类
class Triangle():
    # 实例方法：判断是否为三角形（三边都大于0且两短边之和大于最长边）
    def isTriangle(self,a,b,c):
        maxim=max(a,b,c)
        # 三边都大于0，这里保证了有非正数的数据被排除，确保了数据的合理
        if a>0 and b>0 and c>0:
            # 两短边之和大于最长边
            if maxim<a+b+c-maxim:
                return True
            else:
                return False
        else:
            return False
    # 实例方法：判断是否为直角三角形（先判断是否为三角形，再判断短边的平方之和等于最长边的平方）
    def isRightTriangle(self,a,b,c):
        if self.isTriangle(a,b,c):
            maxim=max(a,b,c)
            if maxim**2==a**2+b**2+c**2-maxim**2:
                return True
            else:
                return False
    # 实例方法：计算三角形面积（海伦公式）
    def area(self,a,b,c):
        p=(a+b+c)/2
        area=((p-a)*(p-b)*(p-c)*p)**(1/2)
        return area
# 变量：记录可以构成直角三角形的数据的组数
count=0
# 构建一个对象Tri
Tri=Triangle()
# 打开文件"整数.txt"
file_0=open("整数.txt","r")
# 从文件中读取数据赋值给列表input_ls
input_ls=file_0.readlines()
# 使i遍历列表input_ls
for i in input_ls:
    # 删除i的结尾的换行符"\n"后，依据","分割字符串后赋值给列表ls
    ls=i.replace('\n','').split(",")
    # 判断这组数据能否构成一个直角三角形
    if Tri.isRightTriangle(eval(ls[0]),eval(ls[1]),eval(ls[2])):
        # 组数+1
        count+=1
        # 输出符合条件的数据
        print(eval(ls[0]),eval(ls[1]),eval(ls[2]))
# 按格式输出
print("共有{}组数据可以构成直角三角形".format(count))
# 关闭文件"整数.txt"
file_0.close()