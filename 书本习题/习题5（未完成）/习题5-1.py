import random
student=set()
choose_num=400
for i in range (1500):
    student.add(i+1)
choose_ls=random.sample(list(student),k=choose_num)
choose_ls=sorted(choose_ls)
for i in range(choose_num):
    choose_ls[i]=str(choose_ls[i])
print("获得学位的学生的编号为：",end='')
print(','.join(choose_ls),end='。')