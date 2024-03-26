S=input("请输入计算式子:")
T=S[3]
FNum=eval(S[0:3])
SNum=eval(S[4::])
print('{}='.format(S),end='')
if T=="+":
    print(FNum+SNum)
elif T=="-":
    print(FNum-SNum)
elif T=="*":
    print(FNum*SNum)
elif T=="/":
    print(FNum/SNum)