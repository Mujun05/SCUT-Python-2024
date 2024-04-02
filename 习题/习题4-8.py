def isPalindromic(n):
    n1=n[::-1]
    if n1==n:
        return True
def getInputs(s):
    x=s.split('，')
    s0=eval(x[0])
    s1=eval(x[1])
    if s0>=s1:
        return False
    return s0,s1
while True:
    try:
        Array=[]
        Area=input("请输入寻找回文数的区间（格式例如n，m。n>m。区间为左闭右闭区间）：")
        X0,X1=getInputs(Area)
        for i in range (X0,X1+1):
            if isPalindromic(str(i)):
                Array.append(str(i))
        print("[{},{}]的所有回文数为：".format(X0,X1),end=(''))
        print("，".join(Array),end="。\n")
    except KeyboardInterrupt:
        print("\n您已通过ctrl+c退出该程序！\n再见！")
        break
    except:
        print("您的输入不符合格式！")