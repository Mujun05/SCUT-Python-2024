# 变量：答案列表
ans_ls=[]
# 变量：阶乘的结果
product=1
# 构造一个从1到100的循环
for i in range(1,101):
    # 阶乘的结果乘i再赋给阶乘的结果
    product*=i
    # 按格式将结果加入列表
    ans_ls.append("{}!={}\n".format(i,product))
# 创建一个文件"阶乘.txt"
file=open("阶乘.txt","w")
# 将答案写入文件"阶乘.txt"
file.writelines(ans_ls)
# 关闭文件"阶乘.txt"
file.close()