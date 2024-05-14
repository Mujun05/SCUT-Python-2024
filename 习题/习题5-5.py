ls0=[26,15,8,8,34,198,242,5,44,5,99,250]
num=eval(input("请输入一个整数:"))
if ls0.count(num)==0:
    print("未找到要查找的数")
else:
    Index_ls=[]
    start=0
    while True:
        try:
            Index_ls.append(ls0.index(num,start,13)+1)
            start=ls0.index(num,start,13)+1
        except:
            break
    print("要查找的数出现的位置是",end="")
    print(Index_ls)