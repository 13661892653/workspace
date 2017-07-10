#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
import random
changeCode=""
for i in range(0,5):
    '''
    随机验证码功能
    '''
    curr=random.randint(0,5)
    if curr==i:
        changeCode+=chr(random.randint(65,90))
    else:
        changeCode+=str(random.randint(1,9))
print('随机6位验证码：',changeCode)

