from random import randint
ls=[]
dic={}
for i in range(16):
    random_num=randint(1,100)
    ls.append(random_num)
    if (i+1)%4==0:
        print(random_num)
    else:
        print(random_num,' ',sep='',end='')
for i in range(16):
    for j in range(i,16):
        dic[ls[i],ls[j]]=ls[i]+ls[j]
print(dic)
