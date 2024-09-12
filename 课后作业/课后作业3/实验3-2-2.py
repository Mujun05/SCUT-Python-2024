Num=eval(input("请输入n的值:"))
e=1
j=1
for i in range(1,Num+1):
    j=j*i
    e=e+(1/j)
print("e的近似值是{}".format(e))