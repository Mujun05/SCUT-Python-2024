Num=input("请输入一个整数:")
if len(Num)!=3:
    print("输入错误")
else:
    print("逆序结果是",end='')
    FNum=Num[-1]
    SNum=Num[-2]
    TNum=Num[-3]
    if FNum=="0" and SNum=="0":
        print('逆序结果是{}'.format(TNum))
    elif FNum=="0":
        print('逆序结果是{}{}'.format(SNum,TNum))
    else:
        print('逆序结果是{}{}{}'.format(FNum,SNum,TNum))