from random import randint as rd
goal0=0
goal1=0
for i in range(100000):
    Num=0
    char=''
    for j in range(3):
        char+=str(rd(1,5))
    Num=int(char)
    if Num%9==0:
        goal0+=1
        if char[0]!=char[1] and char[1]!=char[2] and char[0]!=char[2]:
            goal1+=1
print(goal1/100000,goal0/100000)