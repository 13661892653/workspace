#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
__author__ = "Colby"
import re
'''
计算这表达式的值：1 - 2 * ((60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2)))
'''
def add(express):
    pass
def sub(express):
    pass
def mul(express):
    pass
def div(express):

    return express
def compute(express):
    mul(express)
    div(express)
    add(express)
    sub(express)
def delkuohao(express):
    expr=express
    #检测表达式是否存在括号，如果存在就去括号，否则直接执行
    res=re.compile(r'[()]')
    if res.search(expr):
        #delkuohao(express)
        #匹配括号，然后计算之后替换进去
        sub_expr=re.search('(\([\+\-\*\/\.0-9]+\))',expr).group()
        print('括号最里层的表达式：',sub_expr)
        sub_expr=sub_expr[1:len(sub_expr)-1]
        print('去除左右括号后的的表达式：', sub_expr)
        compute(sub_expr)
        #delkuohao(express)
    else:
        compute(express)

if __name__=="__main__":
    #while True:
    #express=input("请输入要计算的表达式：")
    express='1 - 2 * ((60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2)))'
    print(express)
    '''调用去除括号的函数'''
    delkuohao(express)