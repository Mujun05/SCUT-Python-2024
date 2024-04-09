'''
该方法不符合题目中的要求
但是循环结构确实比递归快
'''
def Fib(n):
    a1=1
    a2=2
    if n==1:
        return a1
    elif n==2:
        return a2
    else:
        for i in range(n-2):
            a2,a1=a2+a1,a2
        return a2
while True:
    try:
        Num=eval(input("请输入台阶的级数："))
        if Num>=100 or Num<=0:
            print("你的输入应大于0且小于等于100")
            continue
        print("青蛙跳上一个{}级的台阶总共有{}种跳法。".format(Num,Fib(Num)))
    except KeyboardInterrupt:
        print("\n您已通过ctrl+c退出该程序！\n再见！")
        break
    except:
        print("您的输入不符合格式！")