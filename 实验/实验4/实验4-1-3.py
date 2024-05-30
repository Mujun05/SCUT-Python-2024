def isPrime(m):
    if m%2==0:
        return False
    else:
        for i in range (3,int(m**(1/2))+1,2):
            if m%i==0:
                return False
        return True
Num0=eval(input("请输入整数m："))
Num1=eval(input("请输入整数n："))
Count=0
for i in range(Num0,Num1+1):
    if isPrime(i):
        Count+=i
print("范围在[{},{}]的素数和为{}".format(Num0,Num1,Count))