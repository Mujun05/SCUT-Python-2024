def CountNumAndStr(InputStr):
    alphabets = 0
    digits = 0
    for Char in InputStr:
        if Char.isalpha():
            alphabets += 1
        elif Char.isdigit():
            digits += 1
    return alphabets, digits
InputStr=input("请输入一个字符串：")
alphabets, digits=CountNumAndStr(InputStr)
print("{}中数字有{}个，英文字母有{}个".format(InputStr,alphabets,digits))