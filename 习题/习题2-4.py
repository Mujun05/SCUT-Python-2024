PointA=input("请输入第一个点的坐标（中间用空格隔开）：")
PointB=input("请输入第二个点的坐标（中间用空格隔开）：")
PointC=input("请输入第三个点的坐标（中间用空格隔开）：")
ArrayA=PointA.split()
ArrayB=PointB.split()
ArrayC=PointC.split()
A_x=eval(ArrayA[0])
A_y=eval(ArrayA[1])
B_x=eval(ArrayB[0])
B_y=eval(ArrayB[1])
C_x=eval(ArrayC[0])
C_y=eval(ArrayC[1])
B_A_x=B_x-A_x
C_A_x=C_x-A_x
B_A_y=B_y-A_y
C_A_y=C_y-A_y
if (B_A_x/C_A_x)!=(B_A_y/C_A_y):
    Area=1/2*abs((B_A_x)*(C_A_y)-(B_A_y)*(C_A_x))
    print('该三角形的面积是：{}'.format(Area))
else:
    print("这三个点构不成一个三角形")
def example():
    input("请输入第{}个点的坐标（中间用空格隔开）：".format())