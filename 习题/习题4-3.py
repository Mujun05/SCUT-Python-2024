import time
def D_to_Y(x):
    x*=6.8
    return x
def Y_to_D(x):
    x/=6.8
    return x
while True:
    try:
        InputNum=input("请输入数目和单位（数目为数字，单位为$或￥）（例如3￥）：")
        Num=eval(InputNum[::len(InputNum)])
        if len(str(Num))!=len(InputNum)-1:
            print("您的输入不符合格式！")
            continue
        Sort=InputNum[-1]
        if Sort=="$":
            Num=D_to_Y(Num)
            print("{}转换后为{:.2f}¥".format(InputNum,Num))
        elif Sort=="¥":
            Num=Y_to_D(Num)
            print("{}转换后为{:.2f}$".format(InputNum,Num))
    except SyntaxError:
        print("您的输入不符合格式！")
    except KeyboardInterrupt:
        print("\n您已通过ctrl+c退出该程序！\n再见！")
        break