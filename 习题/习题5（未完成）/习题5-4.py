from numpy import random
ls=list(random.random(size=eval(input("请输入整数:"))))
for i in range(len(ls)):
    ls[i]=str(ls[i])
print("，".join(ls),end='。')