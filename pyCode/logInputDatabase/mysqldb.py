#coding=utf-8
#!/usr/bin/python
'''
Author:chenlun
Date:2017-04-10
'''
import pymysql
def connDB():
    # 连接数据库
    try:
        conn = pymysql.connect(host='172.16.33.252', user='root', passwd='root', db='xlh_craw', charset='utf8')
        cur = conn.cursor()
        return (conn, cur)
    except Exception as e:
        return "connect Error!"
def exeUpdate(conn, cur, sql):
    '''更新语句，可执行Update，Insert语句'''
    sta = cur.execute(sql)
    conn.commit()
    return (sta)
def exeBath(conn, cur, sql,data):
    '''批量插入数据'''
    #try:
    sta = cur.executemany(sql,data)
    conn.commit()
    return sta
    #except Exception as e:
    #    return pymysql.err
def exeQuery(cur, sql):
    # 查询语句
    cur.execute(sql)
    result = cur.fetchone()
    return result
def connClose(conn, cur):
    # 关闭所有连接
    cur.close()
    conn.close()