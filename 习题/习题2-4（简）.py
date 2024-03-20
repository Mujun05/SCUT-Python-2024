def InquireCoordinate (n) :
    Array = (input ("请输入第{}个点的坐标（中间用,隔开）".format(n))).split(',')
    x = eval (Array[0])
    y = eval (Array[1])
    return x , y
A_x , A_y = InquireCoordinate ("一")
B_x , B_y = InquireCoordinate ("二")
C_x , C_y = InquireCoordinate ("三")
B_A_x=B_x-A_x
C_A_x=C_x-A_x
B_A_y=B_y-A_y
C_A_y=C_y-A_y
if (B_A_x/C_A_x)!=(B_A_y/C_A_y):
    Area=1/2*abs((B_A_x)*(C_A_y)-(B_A_y)*(C_A_x))
    print('该三角形的面积是：{}'.format(Area))
else:
    print("这三个点构不成一个三角形")