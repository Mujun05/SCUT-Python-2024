count = 0
for i in range(1,1000):   
    for j in range(1,i):
        if i%j==0:
            count+=j
    if count == i:
        print(i,"是完数")
    count = 0