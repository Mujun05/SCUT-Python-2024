Num=input("请输入一个整数:")
if len(Num)!=3:
    print("输入错误")
else:
    print("逆序结果是",end='')
    for i in Num[::-1]:
        if i=="0":
            i=i
        else:
            print(i,end='')