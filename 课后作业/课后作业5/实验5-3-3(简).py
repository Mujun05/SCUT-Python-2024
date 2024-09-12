char=input("请输入一个字符串:").replace(' ','')
Frequency_Index_dic={}
for i in list(set(char)):
    Frequency_Index_dic[i]=char.count(i),char.index(i)
sorted_ls=sorted(Frequency_Index_dic.items(),key=lambda x:x[1],reverse=True)
Ans_ls=[]
for i in sorted_ls:
    Ans_ls.append(i[0])
print("不重复的字符是:",end='')
for i in Ans_ls:
    print(i,end='')