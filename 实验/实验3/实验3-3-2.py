Num=eval(input("请输入行数:"))
char1='  '
char2='* '
char3=' '
print((Num-1)*char1,end='')
print(Num*char2)
for i in range(2,Num):
    print((Num-i)*char1,end='')
    print('*',end='')
    print(((2*Num)-3)*char3,end='')
    print('*')
print(Num*char2)