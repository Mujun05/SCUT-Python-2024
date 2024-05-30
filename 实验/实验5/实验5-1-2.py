num=eval(input("请输入数据个数:"))
count=0
enter_set=set()
dis_list=list()
for i in range(num):
    enter=eval(input("请输入数据:"))
    enter_set.add(enter)
    count+=enter
num_list=list(enter_set)
avg=count/num
for j in range(len(num_list)):
    dis_list.append(abs(num_list[j]-avg))
index=dis_list.index(min(dis_list))
print('最接近平均值的数是{}'.format(num_list[index]))