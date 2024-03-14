Year = eval(input("请输入年份："))
if Year%400==0 :
    print('{}年是闰年。'.format(Year))
elif Year%4==0 and Year%100!=0 :
    print('{}年是闰年。'.format(Year))
else :
    print('{}年不是闰年。'.format(Year))