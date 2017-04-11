#coding=utf-8
from pymongo import MongoClient
client =MongoClient()
db=client.Jikexueyuan
coll=db.primer
Jike={'name':'极客','age':'5','skill':'Python'}
god={'name':'玉皇大帝','age':'36','skill':'creatanything','other':'王母娘娘不是他的老婆'}
godslaver={'name':'月老','age':'unKnown','other':'他的老婆叫如来！'}
#coll.insert_one(Jike)
#coll.insert_one(god)
#coll.insert_one(godslaver)
#post_info.remove({'name':u'极客'})
print('操作数据完成')
for item in coll.find():
        print(item)

