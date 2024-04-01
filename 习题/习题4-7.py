def isPerfect(n):
    count = 0
    for j in range(1,i):
        if i%j==0:
            count+=j
    if count == i:
        return True
    else :
        return False
print("10000以内的完数为：",end="")
Array=[]
for i in range(1,10001):   
    if isPerfect(i):
        Array.append(str(i))
print("，".join(Array),end="。")