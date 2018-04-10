#coding=utf-8
import pymongo
def ConnectMongoDB():
    user=''
    pwd=''
    server='localhost'
    port='27017'
    dbName='toutiao'
    url = 'mongodb://' + user + ':' + pwd + '@' + server + ':' + port + '/' + dbName
    #client = pymongo.MongoClient(url)
    client=pymongo.MongoClient('localhost',27017)
    db=client['toutiao']
    data=db['toutiao'].find()
    for i in data:
        print(list(i.keys()))
        return list(i.keys())

def FormatDDL(column,tableName='toutiao'):
    lst=[]
    lst.append('create table %s(' %tableName)
    for col in column:
        lst.append('%s varchar(50) comment '',' %col)
    lst.append('primary key(_id)'
               ')')
    return lst

def main():
    column=ConnectMongoDB()
    print('column',type(column))
    ddlStr=FormatDDL(column)
    for i in ddlStr:
        print(i)
if __name__=="__main__":
    main()