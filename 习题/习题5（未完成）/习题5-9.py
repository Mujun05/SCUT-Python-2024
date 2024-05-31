dic={'admin':'123456','化7':'12345678','强基':'kingking'}
for i in range(2,-1,-1):
    key,value=input("请输入用户名："),input("请输入密码：")
    if key in dic and value==dic[key]:
        print("登陆成功")
        break
    else:
        print("登陆失败")
        print(f"您还有{i}次登陆机会")
        if i==0:
            print("你的登陆机会已用完，程序自动退出！")