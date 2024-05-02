ls0=[26,15,8,8,34,198,242,5,44,5,99,250]
num=eval(input("请输入一个整数:"))
Indexls=[]
start=0
print(ls0.index(num))
while ls0.index(num,start,len(ls0))!=len(ls0):
    start=ls0.index(num,start)
    print
    Indexls.append(start)
print(Indexls)