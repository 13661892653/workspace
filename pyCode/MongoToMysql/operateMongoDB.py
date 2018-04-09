#coding=utf-8
import pymongo

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
print(type(data))
for i in data:
    print(i.keys(),i.values())
    break