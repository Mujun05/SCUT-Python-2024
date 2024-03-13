FirstNum=eval(input("请输入第一个数:"))
SecondNum=eval(input("请输入第二个数:"))
ThirdNum=eval(input("请输入第三个数:"))
MaxNum=max(FirstNum,SecondNum,ThirdNum)
MinNum=min(FirstNum,SecondNum,ThirdNum)
MidNum=FirstNum+SecondNum+ThirdNum-MaxNum-MinNum
print("从小到大的顺序为:",MinNum,MidNum,MaxNum)