Num=eval(input("请输入一个正整数:"))
print(Num,end='')
OneNum=0
while Num>=1:
    if Num%2==1:
        OneNum+=1
        Num=(Num-1)/2
    else:
        Num=Num/2
print('的二进制表示中有{}个1'.format(OneNum))