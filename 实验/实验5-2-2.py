char=input("请输入字符串:")
D={}
for i in char:
    D[i]=D.get(i,0)+1
ls=sorted(D.items(),key=lambda x:x[0])
print("{",end='')
for i in range(len(ls)):
    if i!=len(ls)-1:
        print(f'{ls[i][0]:}:{ls[i][1]},',end='')
    else:
        print(f'{ls[i][0]:}:{ls[i][1]}',end='')
        print("}")