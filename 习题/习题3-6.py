Array=[]
print("1000之内的所有完数为：",end='')
for i in range(1,1000):   
    count = 0
    for j in range(1,i):
        if i%j==0:
            count+=j
    if count == i:
        Array.append(str(i))
print("，".join(Array),end="。")