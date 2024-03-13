import math
FirstNum=eval(input("请输入第一个整数:"))
SecondNum=eval(input("请输入第二个整数:"))
GcdNum=math.gcd(FirstNum,SecondNum)
Num1=FirstNum/GcdNum
Num2=SecondNum/GcdNum
Lcm=math.trunc(Num1*Num2*GcdNum)
print('{}、{}的最小公倍数是{}'.format(FirstNum,SecondNum,Lcm))