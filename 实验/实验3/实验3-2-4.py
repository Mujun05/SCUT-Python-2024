Num = int(input("请输入一个数："))
if Num==1:
    print("1=1")
else:
    print('{}=1'.format(Num),end='*')
i = 2
while i <= Num:
    if i == Num:
        print(i, end="")
        break
    elif Num % i == 0:
        print(i, end="*")
        Num = Num / i
    else:
        i += 1