def is_self_Divisor(Num):
    i=0
    for n in range(0,len(str(Num))):
        if Num[n]=='0':
            return False
        elif eval(Num)%eval(Num[n])==0:
            i+=1
    if i==len(Num):
        return True
    else:
        return False
while True:
    try:
        Array=[]
        Num=input("请输入一个数:")
        for i in range(1,eval(Num)):
            if is_self_Divisor(str(i)):
                Array.append(str(i))
            else:
                continue
        print("{}之内的所有自除数为：".format(Num),end='')
        print("，".join(Array),end="。\n")
    except KeyboardInterrupt:
        print("\n您已通过ctrl+c退出该程序！\n再见！")
        break
    except:
        print("您的输入不符合格式！")