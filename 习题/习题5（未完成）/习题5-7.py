char=input("请输入一个字符串：")
a_set=set(char)
dic={}
for i in a_set:
    dic[i]=char.count(i)
sorted_ls=sorted(dic.items(),key=lambda x:x[0])
print("{",end="")
for i in sorted_ls:
    if i!=sorted_ls[-1]:
        print(f"'{i[0]}':{i[1]}",end=",")
    else:
        print(f"'{i[0]}':{i[1]}"+'}')