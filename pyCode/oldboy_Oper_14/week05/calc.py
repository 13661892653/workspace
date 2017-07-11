#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
__author__ = "Colby"
import re
'''
计算这表达式的值：1 - 2 * ((60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2)))
'''
def format_mark(express):
    express = express.replace('+-', '-')
    express = express.replace('-+', '-')
    express = express.replace('++', '+')
    express = express.replace('--', '+')
    return express
def com_add(express):
    '''
    :param express: 
    :return: 
    '''
    expr = express
    print('17行：', expr)
    sub_expr = re.search(r"\d+\.?\d+[\+\-]\d+\.?\d*", expr)
    print('19行：', sub_expr)
    if not sub_expr:
        print(not sub_expr)
        return expr
    else:
        sub_expr2 = sub_expr.group()
        # print('sub_expr1',sub_expr1,'19行结果express:',div_express)
        if len(sub_expr2.split('+')) > 1:
            n1, n2 = sub_expr2.split('+')
            result = float(n1)+float(n2)
        else:
            n1, n2 = sub_expr2.split('-')
            result = float(n1)-float(n2)
        print('div_result', result)
        re_sub_expr = re.sub(r"\d+\.?\d+\/\d+\.?\d*", str(result), expr, count=1)
        print('26除法表达式替换后：', re_sub_expr)
        # 反复调用除法
        bb = com_add(str(re_sub_expr))
        return bb
def com_div(expr_div):
    '''
    :param expr_div: 
    :return: 
    '''
    expr=expr_div
    print('17行：',expr)
    sub_expr = re.search(r"\d+\.?\d+[\/\*]\d+\.?\d*",expr)
    print('19行：',sub_expr)
    if not sub_expr:
        print(not sub_expr)
        return expr
    else:
        sub_expr2 = sub_expr.group()
        #print('sub_expr1',sub_expr1,'19行结果express:',div_express)
        if len(sub_expr2.split('/')) > 1:
            n1, n2 = sub_expr2.split('/')
            result = float(n1)/float(n2)
        else:
            n1, n2 = sub_expr2.split('*')
            result = float(n1)*float(n2)
        print('div_result',result)
        re_sub_expr=re.sub(r"\d+\.?\d+[\+\-]\d+\.?\d*",str(result),expr,count=1)
        print('26除法表达式替换后：',re_sub_expr)
        #反复调用除法
        bb=com_div(str(re_sub_expr))
        return bb
def compute(express):
    express = com_div(express)
    express = com_add(express)
    return express
def delkuohao(express):
    #检测表达式是否存在括号，如果存在就去括号，否则直接执行
    res=re.compile(r'[()]')
    sub_expr1 = re.search('(\([\+\-\*\/\.0-9]+\))', express)
    print('44行：',sub_expr1)
    if not sub_expr1:
        return express
    else:
        sub_expr1=sub_expr1.group()
        #delkuohao(express)
        #匹配括号，然后计算之后替换进去
        print('括号最里层的表达式：',sub_expr1)
        sub_expr2=sub_expr1[1:len(sub_expr1)-1]
        print('去除左右括号后的表达式：', sub_expr2)
        sub_expr3=compute(sub_expr2)
        print('52行sub_expr3:',sub_expr3)
        sub_expr3 = format_mark(re.sub('(\([\+\-\*\/\.0-9]+\))', str(sub_expr3),express,count=1))
        print('sub_expr3',sub_expr3)
        delkuohao_expr=delkuohao(sub_expr3)
        return delkuohao_expr
if __name__=="__main__":
    #while True:
    #express=input("请输入要计算的表达式：")
    #express = '1-2*((60-30+(-40.0/5/2.0/2)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2)))'
    express='60-30+(-40.0/5/2/4)'
    print(express)
    '''调用去除括号的函数'''
    express=delkuohao(express)
    print('计算结果：',str(express))