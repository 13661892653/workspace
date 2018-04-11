#coding=utf-8
import pymongo
class MongoDB(object):
    def __init__(self,user,password,server,port):
        """
        mongodb=MongoDB('user','password','server','port')
        :param user:
        :param password:
        :param server:
        :param port:
        """
        self.user = user
        self.password = password
        self.server = server
        self.port = port
        self.url = 'mongodb://' + self.user + ':' + self.password + '@' + self.server + ':' + self.port
        self.client = pymongo.MongoClient(self.url)
    def DatabaseNames(self):
        database_names = self.client.database_names()
        return database_names
    def CollectionNames(self):
        collection_names = self.client.collection_names()
        return collection_names

def ConnectMongoDB():
    user=''
    pwd=''
    server='localhost'
    port='27017'
    dbName='jikexueyuan'
    url = 'mongodb://' + user + ':' + pwd + '@' + server + ':' + port + '/' + dbName
    #client = pymongo.MongoClient(url)
    client=pymongo.MongoClient('localhost',27017)
    return client


def FormatDDL(column,tableName):
    lst=[]
    lst.append('''drop table if exists `%s`;''' % tableName)
    lst.append('''create table `%s`(''' %tableName)
    for col in column:
        length=' '*int(50-col.__len__())
        #保证生成的DDL对齐，距离字段名称最左边50个字符对齐。
        lst.append('''\t`%s`%svarchar(50) comment '',''' %(col,length))
    lst.append('''\tprimary key(_id)
    );''')
    return lst

def main():
    client=ConnectMongoDB()
    database_names=client.database_names()
    for database_name in database_names:
        db=client[database_name]
        collection_names=db.collection_names()
        for collection_name in collection_names:
            data=db[collection_name].find()
            for content in data:
                column=list(content.keys())
                ddlStr = FormatDDL(column,collection_name)
                for ddl in ddlStr:
                    print(ddl)
                break

if __name__=="__main__":
    main()