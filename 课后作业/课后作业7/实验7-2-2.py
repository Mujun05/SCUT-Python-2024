# 以只读模式打开2015年5月高三模拟考成绩.csv
f=open("2015年5月高三模拟考成绩.csv","r",encoding="UTF-8")
# 将文件读取为列表并赋值给列表readlines_ls
readlines_ls=f.readlines()
# 创建一个与readlines_ls相同的列表modified_ls（这里不用赋值的原因：赋值是浅拷贝。后续要在循环中删除某些列表中的元素，如果只是用一个列表或赋值都会导致对无用数据的清除干扰）
modified_ls=readlines_ls.copy()
# 是element遍历列表readlines_ls
for element in readlines_ls:
    # 如果element的字符开头不是"3"（即该元素为无用数据），则删除modified_ls中的该元素
    if element[0]!='3':
        modified_ls.remove(element)
# 创建一个待用字典dic
dic={}
# 使element遍历列表modified_ls
for element in modified_ls:
    # 去除换行符\n后，以,为分割符分割字符串element并赋值给列表ls
    ls=element.strip("\n").split(",")
    # 以考号、班级、姓名组成元组为键，计算出的总分为值加入字典dic
    dic[(ls[0],ls[1],ls[2])]=eval(ls[3])+eval(ls[4])+eval(ls[5])+eval(ls[6])+eval(ls[7])+eval(ls[8])
# 以总分为key，降序排列字典dic的键值对并赋值给列表sorted_ls
sorted_ls=sorted(dic.items(),key=lambda x:x[1],reverse=True)
# 按照格式输出结果
print("总分前5名的学生情况")
print("名次  班级   姓名      总分")
# 老师说的30个-
print("-"*30)
for i in range(5):
    # chr(12288)用于对齐中文（符合题目要求）
    print(f"{i+1}     {sorted_ls[i][0][1]}   {sorted_ls[i][0][2]:{chr(12288)}<3}     {sorted_ls[i][1]}")
# 关闭文件
f.close()