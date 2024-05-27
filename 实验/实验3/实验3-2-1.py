Num=eval(input("请输入一个整数:"))
Count = 0
for i in range(1,Num):
    if Num%i==0:
        Count+=i
if Count == Num:
    print("True")
else:
    print("False")