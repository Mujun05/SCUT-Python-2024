Num0=eval(input('请输入第一个正整数:'))
Num1=eval(input('请输入第二个正整数:'))
CountNum=0
for i in range (Num0,Num1+1):
    if i<10:
        if i%10==8:
            CountNum+=1
    else:
        while i//10!=0:
            if i%10==8:
                CountNum+=1
                break
            else:
                i=i//10
print('{}和{}之间有{}个数含有数字8'.format(Num0,Num1,CountNum))