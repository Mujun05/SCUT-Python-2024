f=open("hamlet.txt","r")
dic={}
word_ls=f.read()
replace_element_ls=["!","\"","#","$","%","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","'","{","|","}","~","\n","&"]
for replace_element in replace_element_ls:
    word_ls=word_ls.replace(replace_element," ")
word_ls=word_ls.lower()
word_ls=word_ls.split(" ")
try:
    while True:
        word_ls.remove("")
except ValueError:
    pass
word_set=set(word_ls)
for i in word_set:
    dic[i]=word_ls.count(i)
sorted_ls=sorted(dic.items(),key=lambda x:-x[1])
print("词频最高的10个词为:",end="")
for i in range(10):
    if i==9:
        print(f"{sorted_ls[i][0]}")
    else:
        print(f"{sorted_ls[i][0]}",end=",")