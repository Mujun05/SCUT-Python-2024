def InquireCoordinate (n) :
    Array = (input ("请输入第{}个点的坐标（中间用,隔开）".format(n))).split(',')
    x = eval (Array[0])
    y = eval (Array[1])
    return x , y
A_x , A_y = InquireCoordinate ("一")
B_x , B_y = InquireCoordinate ("二")
C_x , C_y = InquireCoordinate ("三")
AB=((A_x-B_x)**2+(A_y-B_y)**2)**(1/2)
BC=((B_x-C_x)**2+(B_y-C_y)**2)**(1/2)
AC=((A_x-C_x)**2+(A_y-C_y)**2)**(1/2)
p=(AB+BC+AC)/2
if AB+AC<=BC or AB+BC<=AC or AC+BC<=AB:
    print("这三个点构不成一个三角形")
else:
    Area=(p*(p-AB)*(p-AC)*(p-BC))**(1/2)
    print('该三角形的面积是：{}'.format(Area))