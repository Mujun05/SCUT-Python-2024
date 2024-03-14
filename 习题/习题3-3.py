print ("1~100之间能被7整除，但不能被5整除的所有整数为",end='')
for i in range (1,101) :
    if i%7==0 and i%5!=0 :
        print (i,end=' ')
