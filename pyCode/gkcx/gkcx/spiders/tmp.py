import re
# url='https://gkcx.eol.cn/soudaxue/queryProvinceScore.html?page=100'
# res=re.findall('.*?page=(\d+)',url)
# print(res)

res1=[i*500 for i in range(1,8)]
res2=[i*500 for i in range(8,16)]
res3=[i*500 for i in range(16,24)]
res4=[i*500 for i in range(24,32)]
res5=[i*500 for i in range(32,40)]
res6=[i*500 for i in range(40,48)]
res7=[i*500 for i in range(48,56)]
res8=[i*1 for i in range(1,500)]
res9=[i*1 for i in range(501,1000)]
print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
print(res6)
print(res7)
print(res8)
print(res9)