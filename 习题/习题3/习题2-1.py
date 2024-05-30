import math
while True :
    Factorial_Num = input("请输入一个非负整数：")
    if Factorial_Num.isdigit() :
        Factorial_Num = eval (Factorial_Num)
        break
    else :
        print("您输入的不符合要求")
if Factorial_Num == 0 :
    print ("1")
else :
    Factorial_Num = math.factorial(Factorial_Num)
    print (Factorial_Num)