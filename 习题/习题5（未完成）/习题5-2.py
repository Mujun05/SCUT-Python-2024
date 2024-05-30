count=0
char=input("请输入一串包括字符与数字的字符串：")
Inset=set(char)
print("您的输入{}中出现的不同数字有".format(char),end="")
for i in range(10):
    if str(i) in Inset:
        print(i,end='，')
        count+=i
print('这几个数的和为：{}'.format(count))