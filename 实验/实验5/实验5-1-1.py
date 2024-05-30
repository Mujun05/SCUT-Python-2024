countnum=0
char=input("请输入字符串:")
in_set=set(char)
for i in range(10):
    if str(i) in in_set:
        countnum+=i
print('不同的数字和为:{}'.format(countnum))