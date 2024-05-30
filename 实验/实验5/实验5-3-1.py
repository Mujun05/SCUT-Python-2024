char=input("请输入字符串:")
max_char=char[0]
maxim=char.count(char[0])
for i in char[1::]:
    num0=char.count(i)
    if num0>maxim:
        maxim=num0
        max_char=i
print("出现次数最多的字符是{}".format(max_char))