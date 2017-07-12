#!/usr/bin/python
#coding=utf-8
#Author:Lun.Chen
#Version:Python3.6
#Tools :Pycharm 2017.1.2
runStatus=True
if __name__=="__main__":
    salary=input("请填写你的薪水：")
    product=[
                ['bike',1000],
                ['Car',20000],
                ['LV',50000],
                ['egg',50],
                ['apple',50],
                ['tiger',2000],
                ['computer',3000],
                ['cup',10]
            ]
    shoppingCart=[]
    while True:
        print("=================================")
        for i in product:
            print('商品列表>>',product.index(i)+1,':',i[0],i[1])
        print("=================================")
        try:
            goodsNum=input("请选择要购买的商品,输入序号即可：")
            selectGoods = product[int(goodsNum) - 1]
        except IndexError as e:
            print('不存在此商品！')
            continue
        if int(selectGoods[1])>int(salary):
            print('当前余额:',salary,'无法购买',selectGoods[0])
            print('-------------')
            cnt = 1
            for i in shoppingCart:
                print(cnt, i)
                cnt += 1
            print('-------------')
        else:
            salary=int(salary)-int(selectGoods[1])
            print(selectGoods[0],'已经添加到购物车','当前余额：',salary)
            print('购物清单如下：')
            print('-------------')
            shoppingCart.append(selectGoods[0])
            cnt=1
            for i in shoppingCart:
                print(cnt,i)
                cnt+=1
            print('-------------')