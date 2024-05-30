Array=[]
print ("由1、2、3、4这四个数字组成且每位数字各不相同的三位数为：",end='')
for i in range (1,5):
    for j in range (1,5):
        for k in range (1,5):
            if i!=j and j!=k and i!=k:
                CompeteNum=str(i)+str(j)+str(k)
                Array.append(CompeteNum)
print("，".join(Array),end="。")