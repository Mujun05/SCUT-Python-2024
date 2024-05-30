import random
index=[0.6,0.6,0.5,0.5,0.6,0.5,0.6]
count=0
for i in range (100000):
    Awin=0
    Bwin=0
    for j in range (7):
        fNum=random.random()
        if fNum<index[j]:
            Awin+=1
        else:
            Bwin+=1
        if Awin==4 or Bwin==4:
            break
    if Awin==4 and Bwin==1:
        count+=1
print(count/100000)