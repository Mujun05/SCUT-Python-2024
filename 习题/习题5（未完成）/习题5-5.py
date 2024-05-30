ls0=[26,15,8,8,34,198,242,5,44,8,99,250]
num=eval(input("请输入一个整数:"))
count=ls0.count(num)
if count==0:
    print("未找到要查找的数")
else:
    Index_ls=[]
    start=0
    while len(Index_ls)!=count:
        Index_ls.append(str(ls0.index(num,start)+1))
        start=ls0.index(num,start)+1
    print("要查找的数出现的位置是",end="")
    print("[{}]".format(",".join(Index_ls)))