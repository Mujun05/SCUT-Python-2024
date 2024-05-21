ans_ls=[]
product=1
for i in range(1,101):
    product*=i
    ans_ls.append("{}!={}\n".format(i,product))
file=open("阶乘.txt","w")
file.writelines(ans_ls)
file.close()