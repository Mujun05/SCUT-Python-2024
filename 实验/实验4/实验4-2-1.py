import random

s = ""
for i in range(8):
    j = int(62*random.random())
    if j<10:
        s = s + str(j)
    elif j<36:
        s = s + chr(ord("a")+j-10)
    else:
        s = s + chr(ord("A")+j-36)
print("验证码为{}".format(s)) 