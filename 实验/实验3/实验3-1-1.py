First=eval(input("请输入第一个数:"))
Second=eval(input("请输入第二个数:"))
Third=eval(input("请输入第三个数:"))
if First>0 and Second>0 and Third>0:
    if First+Second<=Third or First+Third<=Second or Second+Third<=First:
        print("不能形成三角形")
    elif First==Second==Third:
        print("等边三角形")
    elif First==Second or First==Third or Second==Third:
        print("等腰三角形")
    else:
        print("一般三角形")
else:
    print("不能形成三角形")