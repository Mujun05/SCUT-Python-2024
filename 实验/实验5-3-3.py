char=input("请输入一个字符串:")
Frequency_dic={}
Index_dic={}
All_dic={}
for i in char:
    Frequency_dic[i]=Frequency_dic.get(i,0)+1
for i in list(set(char)):
    Index_dic[i]=char.index(i)
if ' ' in Frequency_dic:
    del Frequency_dic[' ']
if ' ' in Index_dic:
    del Index_dic[' ']
for i in Frequency_dic:
    All_dic[i]=(Frequency_dic.get(i),Index_dic.get(i))
sorted_ls=sorted(All_dic.items(),key=lambda x:x[1],reverse=True)
Ans_ls=[]
for i in sorted_ls:
    Ans_ls.append(i[0])
print("不重复的字符是:",end='')
print(''.join(Ans_ls))