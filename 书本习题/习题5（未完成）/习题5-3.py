from random import randint
def RandomPoint():
    PointTuple=(randint(0,9),randint(0,9))
    return PointTuple
def distance(a,b):
    dis=((a[0]-b[0])**2+(a[1]-b[1])**2)**(1/2)
    return dis
Point_ls=[]
Distance_dic={}
for i in range(10):
    Point_ls.append(RandomPoint())
for i in range(10):
    for j in range(i+1,10):
        Distance_dic[(Point_ls[i],Point_ls[j])]=distance(Point_ls[i],Point_ls[j])
sorted_dic=sorted(Distance_dic.items(),key=lambda x:x[1],reverse=True)
print(f"最大距离是：{sorted_dic[0][1]}相距最远的两个点是：{sorted_dic[0][0][0]}，{sorted_dic[0][0][1]}")