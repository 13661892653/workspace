#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
__author__ = 'colby'
db={
    'engine':'mysql+pymysql',
    'host':'localhost',
    'database':'sms',
    'user':'root',
    'password':'root',
    'encoding':'utf-8',
    'echo':False
}

def MysqlLink():
    linkUrl="\"{pymysql}://{user}:{password}@{host}/{db}\",encoding='{encoding}', echo={echo}".format(
        pymysql=db['engine'],
        user=db['user'],
        password=db['password'],
        host=db['host'],
        db=db['database'],
        encoding=db['encoding'],
        echo=db['echo']
    )
    print(linkUrl)
    return linkUrl