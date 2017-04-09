#coding=utf-8
import pymongo
connection=pymongo.MongoClient()
tdb=connection.Jikexueyuan
post_info=tdb['test']
Jike={'name':'极客','age':'5','skill':'Python'}
god={'name':'玉皇大帝','age':'36','skill':'creatanything','other':'王母娘娘不是他的老婆'}
godslaver={'name':'月老','age':'unKnown','other':'他的老婆叫如来！'}
post_info.save(Jike)
#post_info.save(god)
#post_info.save(godslaver)
#post_info.remove({'name':u'极客'})
print('操作数据完成')
