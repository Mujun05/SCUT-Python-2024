while True:
    ThreeDigits=input("请输入一个三位数:")
    if ThreeDigits.isdigit() and len(ThreeDigits)==3:
        print(ThreeDigits[::-1])
    else:
        print("您的输入不符合标准")