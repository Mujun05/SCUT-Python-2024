def func(a):
    s=0
    for i in range(len(a)):
        s+=eval(a[i])
    return s
Num=input("请输入一个整数:")
print("它的各位数字和为{}".format(func(Num)))