#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
import pymongo
import pymysql


#--------------------------数据库启动函数------------------------------
def start_MySQL():
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='youboy', charset='utf8')
    cur = conn.cursor()
    myConn_list = [conn, cur]
    print('success',myConn_list)
    return myConn_list
#---------------------------------------------------------------------

#--------------------------关闭数据库--------------------------------
def close_MySQL(cur,conn):
    cur.close()
    conn.commit()
    conn.close()
#------------------------------------------------------------------

if __name__ == "__main__":
    user='xlh_data_branch'
    pwd='xlh_data_branch'
    server='43.254.149.60'
    port='27017'
    dbName='xlh_yrtong'
    url = 'mongodb://' + user + ':' + pwd + '@' + server + ':' + port + '/' + dbName
    client = pymongo.MongoClient(url)
    c_enterprise_cash_flow = client[dbName]['enterprise_cash_flow']
    print('c_enterprise_cash_flow',c_enterprise_cash_flow)
    for temple in c_enterprise_cash_flow.find():
        print('data',temple)
    # myConn_list = start_MySQL()
    # cur = myConn_list[1]
    # conn = myConn_list[0]
    #
    # sqli = "replace into ods_mongodb_enterprise(" \
    #        "_id" \
    #        ",catagory_1_Name" \
    #        ",catagory_1_Url" \
    #        ",catagory_2_Name" \
    #        ",catagory_2_Url" \
    #        ",catagory_3_Name" \
    #        ",catagory_3_Url" \
    #        ",cityName,cityUrl" \
    #        ",contactPerson" \
    #        ",enterpriseAddr" \
    #        ",enterpriseFax" \
    #        ",enterpriseMobile" \
    #        ",enterpriseName" \
    #        ",enterprisePhone" \
    #        ",enterpriseUrl" \
    #        ",provinceName" \
    #        ",url) " \
    #        "values(%s,%s,%s,%s,%s" \
    #        ",%s,%s,%s,%s,%s" \
    #        ",%s,%s,%s,%s,%s" \
    #        ",%s,%s,%s)"
    # #print('sqli',sqli)
    # dataList=[]
    # for temple in enterprise_collect.find():
    #     print(temple['_id'])
    #     #print('temple',temple)
    #     data=(str(temple['_id']),
    #             temple['catagory_1_Name'],
    #             temple['catagory_1_Url'],
    #             temple['catagory_2_Name'],
    #             temple['catagory_2_Url'],
    #             temple['catagory_3_Name'],
    #             temple['catagory_3_Url'],
    #             temple['cityName'],
    #             temple['cityUrl'],
    #             temple['contactPerson'],
    #             temple['enterpriseAddr'],
    #             temple['enterpriseFax'],
    #             temple['enterpriseMobile'],
    #             temple['enterpriseName'],
    #             temple['enterprisePhone'],
    #             temple['enterpriseUrl'],
    #             temple['provinceName'],
    #             temple['url'])
    #     dataList.append(data)
    # #print('dataList', dataList)
    #
    # cur.executemany(sqli,dataList)
    # #conn.commit()
    # close_MySQL(cur, conn)