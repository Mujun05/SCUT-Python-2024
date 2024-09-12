#题目可转换为a1=1,a2=2的斐波那契型数列{an}
def Fib(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return Fib(n-1)+Fib(n-2)
while True:
    try:
        Num=eval(input("请输入台阶的级数："))
        if Num>=100:
            print("你的输入应小于等于100")
            continue
        print("青蛙跳上一个{}级的台阶总共有{}种跳法。".format(Num,Fib(Num)))
    except KeyboardInterrupt:
        print("\n您已通过ctrl+c退出该程序！\n再见！")
        break
    except:
        print("您的输入不符合格式，请重新输入！")