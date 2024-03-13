Character=input("请输入字符：")
LengthMult2=2*len(Character)
print(Character*4)
for i in range(LengthMult2):
    print('{:<4 b}{:>4}'.format(Character,Character))
print(Character*4)