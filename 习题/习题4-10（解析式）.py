from math import factorial
from math import floor
def Fib(n):
    Result=0
    for i in range(floor(n/2)+1):
        Result+=factorial(n-i)/(factorial(i)*factorial(n-2*i))
    return Result
while True:
    try:
        Num=eval(input("请输入台阶的级数："))
        if Num>=100 or Num<=0:
            print("你的输入应大于0且小于等于100")
            continue
        print("青蛙跳上一个{}级的台阶总共有{:.0f}种跳法。".format(Num,Fib(Num)))
    except KeyboardInterrupt:
        print("\n您已通过ctrl+c退出该程序！\n再见！")
        break
    except:
        print("您的输入不符合格式！")