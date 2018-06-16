#coding=utf-8
#author:colby
import tushare as ts
def main():
    result=ts.get_hs300s()
    print(result)


if __name__ == "__main__":
    main()

