#coding=utf-8
#author:colby
import tushare as ts
#http://tushare.org/
#安装：pip install tushare
#TuShare包是一个免费、开源的Python财经数据接口包
def main():
    #沪深TOP300
    hs300s=ts.get_hs300s()
    #沪深上市公司基本情况
    stock_basics=ts.get_stock_basics()
    print(hs300s)
    print(stock_basics)


if __name__ == "__main__":
    main()

