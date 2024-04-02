def drawPic(n,char):
    if ord(char)>64:
        Indexstr=' '
    else:
        Indexstr=' '
    i=1
    while i <= n:
        print((n-i)*Indexstr,end='')
        print((2*i-1)*char,end='')
        print((n-i)*Indexstr,end='\n')
        i+=1
drawPic(5,'、')