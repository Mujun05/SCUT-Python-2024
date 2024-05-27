Num=eval(input("请输入一个正整数:"))
BinaryNum=bin(Num)
OneNum=0
for i in BinaryNum:
    if i=='1':
        OneNum+=1
print('{}的二进制表示中有{}个1'.format(Num,OneNum))