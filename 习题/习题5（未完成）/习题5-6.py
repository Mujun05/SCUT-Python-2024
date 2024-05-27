from random import randint
ls0=[]
dic={}
for i in range(16):
    rand_num=randint(1,100)
    if (i+1)%4==0:
        print(rand_num)
    else:
        print(rand_num,end=' ')
    ls0.append(rand_num)
for j in range(16):
    for k in range(j+1,16):
        dic[(j,k)]=ls0[j]+ls0[k]
sorted_ls=sorted(dic.items(),key=lambda x:x[1],reverse=True)
for l in range(16):
    for m in range(l+1,16):
        if sorted_ls[l][1]==sorted_ls[m][1]:
            print(f"{ls0[sorted_ls[l][0][0]]}+{ls0[sorted_ls[l][0][1]]}={ls0[sorted_ls[m][0][0]]}+{ls0[sorted_ls[m][0][1]]}")