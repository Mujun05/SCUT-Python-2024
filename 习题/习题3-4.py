Array=[]
print ('100~999之间的水仙花数为：',end='')
for i in range (100,1000) :
    iStr = str(i)
    FirstNum = eval(iStr[0])
    SecondNum = eval(iStr[1])
    ThirdNum = eval(iStr[2])
    if FirstNum**3+SecondNum**3+ThirdNum**3==i :
        Array.append(str(i))
print("，".join(Array),end="。")