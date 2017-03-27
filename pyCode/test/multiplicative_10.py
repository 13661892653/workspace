#coding=utf-8
#10以内乘法口诀
a,b=1,1
string=""
while a<10:
    b=a
    while b>=1:
        string=str(a)+'x'+str(b)+'='+str(a*b)+','+string
        b-=1
    print(string[0:len(string)-1])
    string=""
    a+=1