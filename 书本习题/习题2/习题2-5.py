import time

t0 = time.time()
s = '实现中华民族伟大复兴'
scale = len (s)
print("{:-^20}".format('执行开始'))
r = ""
for i in range (scale+1):
    b = '..'*(scale-i)
    c = (i/scale)*100
    t1 = time.time()
    print("{:^3.0f}%[{}->{}]{:.2f}s".format(c,r,b,t1-t0))
    if i >= scale :
        r = s
    else :
        r+=s[i]
    time.sleep(0.1)
print("\n"+"{:-^20}".format('执行结束'))