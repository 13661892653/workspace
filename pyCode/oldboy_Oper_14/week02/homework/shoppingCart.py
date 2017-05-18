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
        for i in product:
            print('>>',product.index(i)+1,':',i[0],i[1])
        goodsNum=input("请选择商品,输入序号即可：")
        selectGoods=product[int(goodsNum)-1]
        print(selectGoods)
