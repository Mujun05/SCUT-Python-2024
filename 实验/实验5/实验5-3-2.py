import random
# 引入随机数库
random.seed(10079)
# 设定随机数种子
dic={}
Ans_ls=[]
Index=0
# 创建所有待用变量
for i in range(1000):
    Rand_Num=random.randint(100,200)
    dic[Rand_Num]=dic.get(Rand_Num,0)+1
    # 生成随机数并将它和它的频数写入字典
sorted_ls=sorted(dic.items(),key=lambda x:x[1],reverse=True)
# 按频数降序导出为已排序列表
while True:
    Ans_ls.append(str(sorted_ls[Index][0]))
    # 将频数最大的数加入答案列表
    # str()将整型int转化为字符串型str，原因见最后一行！！！
    if sorted_ls[Index][1]==sorted_ls[Index+1][1]:
        Index+=1
        # 如果已排序列表的后一位数与前一位数的频数相同，则索引加一，继续循环。
    else:
        break
if len(Ans_ls)==len(sorted_ls):
    Ans_ls.clear()
    print("没有众数")
    # 若所有数的频数都相等，则没有众数。
    # 这一段几乎不可能发生
else:
    print("众数是",end=' ')
    print(" ".join(Ans_ls))
    # "char"join(ls)将列表ls中的元素用字符串char分割并返回一个字符串
    # 这时ls中的所有元素都要是字符串型！！！