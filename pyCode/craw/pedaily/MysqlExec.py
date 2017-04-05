#coding=utf-8
import pymysql
'''
程序名称   :MysqlExec.py
功能       :执行Mysql增删改查语句
开发工具   :PyCharm 2016.3.2
Python版本 :Python 3.5.2
开发人     :chenlun
创建时间   :2017-03-08
'''
class MysqlExec():
    def __init__(self,conn,cur,sql):
        self.connect=conn
        self.cursor=cur
        self.sqlstate=sql
    def connDB(self):
        # 连接数据库
        conn = pymysql.connect(host='172.16.33.252', user='root', passwd='root', db='xlh_craw', charset='utf8')
        cur = conn.cursor()
        return (conn, cur)

    def exeUpdate(self):
        # 更新语句，可执行Update，Insert语句
        sta = self.cur.execute(self.sql)
        self.conn.commit()
        return (sta)

    def exeQuery(self):
        # 查询语句
        self.cur.execute(self.sql)
        result = self.cur.fetchone()
        return result

    def connClose(self):
        # 关闭所有连接
        self.cur.close()
        self.conn.close()