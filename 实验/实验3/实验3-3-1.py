Num=eval(input("请输入行数："))
char1=' '
char2='*'
i=1
while i<=Num:
    print((Num-i)*char1,end='')
    print(((2*i)-1)*char2,end='')
    print((Num-i)*char1)
    i+=1