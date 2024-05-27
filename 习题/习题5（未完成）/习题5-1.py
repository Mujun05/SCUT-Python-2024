import random

student=set()
for i in range (1500):
    student.add(i+1)
a=random.sample(list(student),k=400)
a=sorted(a)
for i in range(400):
    a[i]=str(a[i])
print("获得学位的学生的编号为：",end='')
print('''',''''.join(a),end='。')