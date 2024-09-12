def is_self_power(k):
    SumNum=0
    n=len(str(k))
    for i in range(0,n):
        SumNum=SumNum+(eval(str(k)[i]))**n
    if SumNum==k:
        return True
    else:
        return False
Array=[]
for i in range(1000,10000):
    if is_self_power(i):
        Array.append(str(i))
print("所有的4叶玫瑰数为：",end="")
print("，".join(Array),end="。")