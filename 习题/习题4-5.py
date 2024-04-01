def is_prime(k):
    if k%2==0:
        return False
    else:
        for i in range (3,k,2):
            if k%i==0:
                return False
        return True
while True:
    try:
        Num=eval(input("请输入一个>2的正偶数："))
        if Num%2==1:
            print("Data error!")
            continue
        for k in range (3,Num,2):
            if is_prime(k):
                if is_prime(Num-k):
                    print("{}={}+{}".format(Num,k,Num-k))
                    break
    except KeyboardInterrupt:
        print("\n您已通过ctrl+c退出该程序！\n再见！")
        break
    except:
        print("Data error!")