desc formatted dw.full_h_usr_base_user;
dfs -ls dfs -ls hdfs://BIGDATA:9000/user/hive/warehouse/dw.db/full_h_usr_base_user;
dfs -rmdir dfs -ls hdfs://BIGDATA:9000/user/hive/warehouse/dw.db/full_h_usr_base_user;

#192.168.1.181 192.168.1.1
#创建外表
create external table dw.full_h_usr_base_user(
user_id  string    comment '用户id',
reg_ip   string    comment 'ip',
reg_ip_geo_map map<string,string> comment 'city_id,city_name,isp,province_id,province_name,country_id,country_name,postzip,district,province'
)
comment '用户测试表'
partitioned by(ds string comment '当前时间,用于分区字段')
row format delimited
fields terminated by '\t'
collection items terminated by ","
map keys terminated by ":"
stored as TEXTFILE;


#加载数据
load data local inpath '/opt/data/dw.full_h_usr_base_user.del' 
overwrite into table dw.full_h_usr_base_user partition(ds='2017-09-25');


#Python UDF函数ip_to_num.py
#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
import socket
import struct
import sys,datetime
ipDB='/opt/data/IP_utf-8.csv'
for line in sys.stdin:
    line = line.strip()
    user_id, reg_ip, reg_ip_geo_map, ds = line.split('\t')
    num_ip = int(socket.ntohl(struct.unpack("I", socket.inet_aton(str(reg_ip)))[0]))
    f = open(ipDB, 'r', encoding="utf-8")
    ipDict = {}
    count = 0
    for line in f:
        if count == 9:
            count += 1
            continue
        line = line.split(',')
        if int(line[2]) <= num_ip and int(line[3]) >= num_ip:
            ipDict['IP'] = reg_ip
            ipDict['nationality'] = line[4]
            ipDict['province'] = line[5]
            ipDict['city'] = line[6]
            ipDict['Corporation'] = line[8]
            reg_ip_geo_map=str(ipDict)[1:-1].replace('\'','').replace(' ','')
            print('\t'.join([user_id, reg_ip, reg_ip_geo_map,ds]))
    f.close()


#上传文件到fywyqu 
/opt/udf/ip_to_num.py

#hive
add file /opt/udf/ip_to_num.py;
#Added resources: [/opt/udf/ip_to_num.py]

#测试自定义函数的SQL语句
SELECT
  TRANSFORM (user_id, reg_ip, reg_ip_geo_map, ds)
  USING 'python3 ip_to_num.py'
  AS (user_id, reg_ip, reg_ip_geo_map, ds)
FROM dw.full_h_usr_base_user;

#数据覆盖到dw.full_h_usr_base_user
set hive.exec.dynamic.partition.mode=nonstrict;
insert overwrite table dw.full_h_usr_base_user partition(ds)
select user_id
,reg_ip
,str_to_map(reg_ip_geo_map,',',':') as reg_ip_geo_map
,ds from (
SELECT
  TRANSFORM (user_id, reg_ip, reg_ip_geo_map,ds)
  USING 'python3 ip_to_num.py'
  AS (user_id, reg_ip, reg_ip_geo_map,ds)
FROM dw.full_h_usr_base_user
) as a
;

#查询字典数据

select user_id
,reg_ip_geo_map['province'] 
,reg_ip_geo_map['city'] 
,reg_ip_geo_map['nationality'] 
from dw.full_h_usr_base_user
where ds='2017-09-25' and user_id='1000000015';


输出结果：
OK
1000000015      安徽省  合肥市  中国
Time taken: 0.107 seconds, Fetched: 1 row(s)
#动态分区，将字符创转换成MAP
#set hive.exec.dynamic.partition.mode=nonstrict;
#insert into dw.full_h_usr_base_user partition(ds) 
#select user_id
#, reg_ip
#, str_to_map(reg_ip_geo_map) reg_ip_geo_map
#,ds from dw.full_h_usr_base_user_tmp;