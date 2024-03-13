while True:
    ThreeDigits=input("请输入一个三位数:")
    if ThreeDigits.isdigit() and len(ThreeDigits)==3:
        print(ThreeDigits[::-1])
        input("输入任意键并回车退出程序。")
        break
    else:
        print("您的输入不符合标准")