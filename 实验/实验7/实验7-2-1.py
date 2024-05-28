""" 
编写以下三个函数并依次调用，注意在每个函数内部打开文件并关闭。
(1)定义函数def f_write()：用随机函数生成10行数据，每行数据个数3到8个不等，每个整数的范围为[-50,50]。把这些数据保存为data.txt
(2)定义函数def f_read()，用read函数求文件data.txt中全部数字的最大值(不能用max,sort函数)，并输出
(3)定义函数def f_readlines(),用readlines()函数读文件，计算文件data.txt每一行各个数的和，并输出和的最大值
"""
# 引入随机库random
import random
# 设置随机种子
random.seed(1000)

# 函数f_write()：用随机函数生成10行数据，每行数据个数3到8个不等，每个整数的范围为[-50,50]。把这些数据保存为data.txt
def f_write():
    # 以覆盖写模式打开文件data.txt
    f=open("data.txt","w",encoding="UTF-8")
    # 创建一个待用列表ls
    ls=[]
    # 创建一个10次的循环
    for i in range(10):
        # 生成该行数据的个数并创建一个循环
        nums=random.randint(3,8)
        for j in range(nums):
            # 将该行数据存入列表ls中
            ls.append(str(random.randint(-50,50)))
        # 将数据按照格式写入data.txt
        char="，".join(ls)+"\n"
        f.write(char)
        # 清空待用列表ls
        ls.clear()
    # 关闭文件data.txt
    f.close()

# 调用函数f_write()
f_write()

# 函数f_read():用read函数求文件data.txt中全部数字的最大值(不能用max,sort函数)，并输出
def f_read():
    # 以只读模式打开文件data.txt
    f=open("data.txt","r")
    # 用read函数读出文件并赋值给字符串char
    char=f.read()
    # 以\n为分割符分割字符串char并赋值给列表row_ls
    row_ls=char.split("\n")
    # 删除row_ls的最后一项（因为这一项是个空字符串！！！）
    del row_ls[-1]
    # 创建一个待用变量maximum（最大值），将其赋值为-51（确保它一定小于任何数据）
    maximum=-51
    # 使row遍历列表row_ls
    for row in row_ls:
        # 以，为分割符分割字符串row并赋值给列表element_ls
        element_ls=row.split("，")
        # 创建一个待用变量Local_maximum（局部最大值），将其赋值为element_ls的第0项
        Local_maximum=eval(element_ls[0])
        # 使element遍历element_ls除了第0项
        for element in element_ls[1::]:
            # 如果element大于Local_maximum，则将element赋值给Local_maximum
            if eval(element)>Local_maximum:
                Local_maximum=eval(element)
        # 如果Local_maximum大于maximum，则将Local_maximum赋值给maximum
        if Local_maximum>maximum:
            maximum=Local_maximum
    # 输出全部数字的的最大值
    print(f"全部数字的的最大值为{maximum}")
    # 关闭文件data.txt
    f.close()

# 调用函数f_read()
f_read()

# 函数f_readlines()：用readlines()函数读文件，计算文件data.txt每一行各个数的和，并输出和的最大值
def f_readlines():
    # 以只读模式打开文件data.txt
    f=open("data.txt","r")
    # 用readlines函数读出文件并赋值给列表row_ls
    row_ls=f.readlines()
    # 创建一个待用变量maximum_count（和的最大值），将其赋值为-408（确保它一定小于任何和）
    maximum_count=-408
    # 使row遍历列表row_ls
    for row in row_ls:
        # 以，为分割符分割字符串row并赋值给列表element_ls
        element_ls=row.split("，")
        element_ls=row.strip("\n").split("，")
        # 创建一个待用变量Local_count（局部和），将其赋值为0
        Local_count=0
        # 使element遍历element_ls，用于求和该行数据
        for element in element_ls:
            Local_count+=eval(element)
        # 如果Local_count大于maximum_count，则将Local_count赋值给maximum_count
        if Local_count>maximum_count:
            maximum_count=Local_count
    # 输出每一行各个数的和的最大值
    print(f"每一行各个数的和的最大值为{maximum_count}")
    # 关闭文件data.txt
    f.close()

# 调用函数f_readlines()
f_readlines()