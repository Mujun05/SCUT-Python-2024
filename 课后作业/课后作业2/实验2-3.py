FirstSide=eval(input("请输入第一条边:"))
SecondSide=eval(input("请输入第二条边:"))
ThirdSide=eval(input("请输入第三条边:"))
p=(FirstSide+SecondSide+ThirdSide)/2
Area=(p*(p-FirstSide)*(p-SecondSide)*(p-ThirdSide))**0.5
print("由",'{}、{}、{}构成的三角形面积为:{}'.format(FirstSide,SecondSide,ThirdSide,format(Area, '.2f')))