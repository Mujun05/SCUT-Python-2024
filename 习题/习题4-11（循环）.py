def Fib(n):
    a1=1
    a2=1
    if n==1 or n==2:
        return 1
    else:
        for i in range(n-2):
            a2,a1=a2+a1,a2
        return a2
try:
    Num=eval(input("请输入整数N："))
    print("斐波那契数列的第{}项为{}".format(Num,Fib(Num)))
except KeyboardInterrupt:
    print("\n您已通过ctrl+c退出该程序！\n再见！")
except:
    print("您的输入不符合格式！")