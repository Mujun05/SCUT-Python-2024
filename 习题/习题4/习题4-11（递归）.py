def Fib(n):
    if n==1 or n==2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
try:
    Num=eval(input("请输入整数N："))
    print("斐波那契数列的第{}项为{}".format(Num,Fib(Num)))
except KeyboardInterrupt:
    print("\n您已通过ctrl+c退出该程序！\n再见！")
except:
    print("您的输入不符合格式！")