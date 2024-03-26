FNum=eval(input("输入开始数字:"))
SNum=eval(input("输入结束数字:"))
TotalNum=SNum-FNum+1
for i in range(1,TotalNum+1):
    if i==TotalNum:
        print(FNum)
    elif i%5!=0:
        print(FNum,end=',')
    else:
        print(FNum)
    FNum+=1