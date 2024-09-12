Num=eval(input("请输入一个正整数:"))
BinaryNum=str(bin(Num))
OneNum=BinaryNum.count("1")
print('{}的二进制表示中有{}个1'.format(Num,OneNum))