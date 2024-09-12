def DrawPic(n,char):
    space=' '
    for i in range(1,n):
        print(space*(n-i)+char*(2*i-1))
    print(char*(2*n-1))
    for i in range(1,n):
        print(space*(i)+char*(2*(n-i)-1))
    pass
Num=eval(input("请输入一个整数:"))
char=input("请输入一个字符:")
DrawPic(Num,char)