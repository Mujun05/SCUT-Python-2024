x0=input('请输入开始字母:')
x1=input('请输入结束字母:')
p0=ord(x0)
p1=ord(x1)
s=''
if p0>p1:
    p0,p1=p1,p0
for i in range(p0,p1+1):
    s+=chr(i)
for j in range(len(s)):
    print(s[j::],end='')
    print(s[:j])