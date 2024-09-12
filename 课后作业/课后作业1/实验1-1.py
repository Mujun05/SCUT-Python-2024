import math
radius = eval(input(" 请输入半径："))
girth = 2 * math.pi * radius
area = math.pi * radius * radius
volume = 4 * math.pi * radius * radius * radius / 3
print (" 半径 = ", radius)
print (" 周长 = ", girth)
print (" 面积 = ", area)
print (" 体积 = ", volume)