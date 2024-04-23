from random import randint
def RandomPoint():
    PointTuple=(randint(0,9),randint(0,9))
    return PointTuple
def distance(a,b):
    dis=((a[0]-b[0])**2+(a[1]-b[1])**2)**(1/2)
    return dis
PointList=[]
DistanceList=[]
for i in range(10):
    PointList.append(RandomPoint())
for j in range(10):
    for k in range(j+1,10):
        DistanceList.append(distance(PointList[j],PointList[k]))
MaxDis=max(DistanceList)
print("最大距离是：{}，".format(MaxDis),end='')
Index=DistanceList.index(MaxDis)
if Index<=8:
    print("相距最远的两个点是：{}，{}。".format(PointList[0],PointList[Index+1]))
elif Index<=16:
    print("相距最远的两个点是：{}，{}。".format(PointList[1],PointList[Index-7]))
elif Index<=23:
    print("相距最远的两个点是：{}，{}。".format(PointList[2],PointList[Index-14]))
elif Index<=29:
    print("相距最远的两个点是：{}，{}。".format(PointList[3],PointList[Index-20]))
elif Index<=34:
    print("相距最远的两个点是：{}，{}。".format(PointList[4],PointList[Index-25]))
elif Index<=38:
    print("相距最远的两个点是：{}，{}。".format(PointList[5],PointList[Index-29]))
elif Index<=41:
    print("相距最远的两个点是：{}，{}。".format(PointList[6],PointList[Index-32]))
elif Index<=43:
    print("相距最远的两个点是：{}，{}。".format(PointList[7],PointList[Index-34]))
elif Index<=44:
    print("相距最远的两个点是：{}，{}。".format(PointList[8],PointList[Index-35]))