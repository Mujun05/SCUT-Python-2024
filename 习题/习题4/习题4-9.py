def drawPic(n,char):
    if len(char)!=1:
        print("您的输入长度错误！")
        return False
    tuple1=tuple("·\"`1234567890-=qwertyuiop[]\ asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?“”")
    if char in tuple1:
        Indexstr=' '
    else:
        Indexstr='  '
    i=1
    while i <= n:
        print((n-i)*Indexstr,end='')
        print((2*i-1)*char,end='')
        print((n-i)*Indexstr)
        i+=1
    i-=1
    while i>=1:
        i-=1
        print((n-i)*Indexstr,end='')
        print((2*i-1)*char,end='')
        print((n-i)*Indexstr)
while True:
    try:
        drawPic(eval(input("请输入行数n：")),input("请输入打印字符："))
    except KeyboardInterrupt:
        print("\n您已通过ctrl+c退出该程序！\n再见！")
        break
    except SyntaxError:
        print("您的输入不符合格式！")
    except NameError:
        print("您的输入不符合格式！")