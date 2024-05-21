class Triangle():
    def isTriangle(self,a,b,c):
        maxim=max(a,b,c)
        if a>0 and b>0 and c>0:
            if maxim<a+b+c-maxim:
                return True
            else:
                return False
        else:
            return False
    def isRightTriangle(self,a,b,c):
        maxim=max(a,b,c)
        if maxim**2==a**2+b**2+c**2-maxim**2:
            return True
        else:
            return False
    def area(self,a,b,c):
        p=(a+b+c)/2
        area=((p-a)*(p-b)*(p-c)*p)**(1/2)
        return area
count=0
file_0=open("整数.txt","r")
input_ls=file_0.readlines()
for i in input_ls:
    ls=i.replace('\n','').split(",")
    Tri=Triangle()
    if Tri.isTriangle(eval(ls[0]),eval(ls[1]),eval(ls[2])):
        if Tri.isRightTriangle(eval(ls[0]),eval(ls[1]),eval(ls[2])):
            count+=1
            print(eval(ls[0]),eval(ls[1]),eval(ls[2]))
print("共有{}组数据可以构成直角三角形".format(count))
file_0.close()