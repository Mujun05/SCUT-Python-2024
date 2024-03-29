def ComputeDistance(x,y,z):
    Distance=(x**2+y**2+z**2)**(1/2)
    return Distance
try:
    Array=(input("请输入A点的三维坐标(以,分隔):")).split(',')
    x=eval(Array[0])
    y=eval(Array[1])
    z=eval(Array[2])
    print('A点距远点的欧式距离为{:2f}'.format(ComputeDistance(x,y,z)))
except TypeError:
    print("坐标应如x,y,z所示，其中x、y、z都应为数字")