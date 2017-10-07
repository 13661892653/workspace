create external table dw.full_h_usr_base_user(
user_id  string    comment '用户id',
reg_ip  string    comment 'ip',
reg_ip_geo_map map<string,string> comment
'city_id,city_name,isp,province_id,province_name,country_id,country_name,postzip,district,province'
)
comment '用户测试表'
partitioned by(ds string comment '当前时间,用于分区字段')
row format delimited
fields terminated by '\t'
collection items terminated by ","
map keys terminated by ":"
stored as TEXTFILE;

SQOOP1.4.6配置环境变量/etc/profile
export SQOOP_HOME=/app/sqoop-1.4.6
export PATH=$SQOOP_HOME/bin:$PATH


服务器信息：
192.168.1.101 windows7 mysql world数据库的country表

Mysql-->Hadoop
sqoop import \
--connect jdbc:mysql://192.168.1.101:3306/etlmonitor \
--username root \
--password root \
--table etl_job_log \
--target-dir /etl/input/etl_job_log

查看数据导入结果：
[root@BIGDATA bin]# hadoop fs -cat /etl/input/etl_job_log/part-*
19,WAITING,JOB001-HQL,2017-09-14,2017-09-16,00:00:00,2017-09-16,00:00:00, ,0,0,0
20,WAITING,JOB002-SQL,2017-09-15,2017-09-16,00:00:00,2017-09-16,00:00:00, ,0,0,0
21,WAITING,JOB004-SHELL,2017-09-16,2017-09-16,00:00:00,2017-09-16,00:00:00, ,0,0,0
22,WAITING,JOB003-KETTLE,2017-09-17,2017-09-16,00:00:00,2017-09-16,00:00:00, ,0,0,0
23,WAITING,JOB004-SHELL,2017-09-17,2017-09-16,00:00:00,2017-09-16,00:00:00, ,0,0,0
24,WAITING,JOB005-PYTHON,2017-09-17,2017-09-16,00:00:00,2017-09-16,00:00:00, ,0,0,0


Hadoop-->Mysql
sqoop export \
--connect jdbc:mysql://192.168.1.101:3306/etlmonitor \
--username root \
--password root \
--table etl_job_log \
--export-dir /etl/input/etl_job_log
查看数据导出结果：
1	WAITING	JOB001-HQL	2017-09-14	2017-09-16	00:00:00	2017-09-16	00:00:00	 	0	0	0
2	WAITING	JOB002-SQL	2017-09-15	2017-09-16	00:00:00	2017-09-16	00:00:00	 	0	0	0
3	WAITING	JOB004-SHELL	2017-09-16	2017-09-16	00:00:00	2017-09-16	00:00:00	 	0	0	0
4	WAITING	JOB003-KETTLE	2017-09-17	2017-09-16	00:00:00	2017-09-16	00:00:00	 	0	0	0
5	WAITING	JOB004-SHELL	2017-09-17	2017-09-16	00:00:00	2017-09-16	00:00:00	 	0	0	0
6	WAITING	JOB005-PYTHON	2017-09-17	2017-09-16	00:00:00	2017-09-16	00:00:00	 	0	0	0
19	WAITING	JOB001-HQL	2017-09-14	2017-09-16	00:00:00	2017-09-16	00:00:00	 	0	0	0
20	WAITING	JOB002-SQL	2017-09-15	2017-09-16	00:00:00	2017-09-16	00:00:00	 	0	0	0
21	WAITING	JOB004-SHELL	2017-09-16	2017-09-16	00:00:00	2017-09-16	00:00:00	 	0	0	0
22	WAITING	JOB003-KETTLE	2017-09-17	2017-09-16	00:00:00	2017-09-16	00:00:00	 	0	0	0
23	WAITING	JOB004-SHELL	2017-09-17	2017-09-16	00:00:00	2017-09-16	00:00:00	 	0	0	0
24	WAITING	JOB005-PYTHON	2017-09-17	2017-09-16	00:00:00	2017-09-16	00:00:00	 	0	0	0


导入Mysql所有表到Hadoop平台
sqoop import-all-tables \
--connect jdbc:mysql://192.168.1.101:3306/etlmonitor \
--username root \
--password root \
--warehouse-dir /user/hive/warehouse/dw.db/


创建内表：
drop table dw.etl_job_log;
CREATE TABLE dw.etl_job_log
(
JOB_SEQ_ID string,
JOB_STS string,
JOB_NM string,
DATA_PRD string,
ACT_ST_DT string,
ACT_ST_TM string,
ACT_ED_DT string,
ACT_ED_TM string,
JOB_LG string,
RW_RD string,
RW_IST string,
RW_UPT string
)
comment '用户测试表'
row format delimited
fields terminated by ','
stored as TEXTFILE;

/user/hive/warehouse/dw.db/etl_job_log/
/user/hive/warehouse/dw.db

Mysql数据直接导入Hive
注意事项：
1、目标目录必须为空，hive不会清空数据再插入
2、如果是分区表，必须指定分区
3、字段分隔符必须跟hive表定义的保持一致，否则数据显示会有问题
4、--null-string '**' 表示，对于空的单元格用什么表示，这里是用**表示。  不能用--表示。会报错，因为--是特有字符
5、-m 1:表示启动几个map来执行，默认4个，这和最后产生几个文件也有关系，应该是启动一个map，产生一个文件。
6、--append 如果该命令重复执行，会报错==>说该文件已经在目录中存在了，但是加上--append之后，就可以重复执行了，并且每次执行会产生新的文件。
7、--hive-import：表示导入到hive中。
8、--check-column 'TBL_ID':表示增量导入的时候，需要验证的列，也就是说，当这一列有新增的时候，我们才导入。
9、--incremental append：表示，增量导入的时候，出现增量的时候这么处理， 这里的append表示出现增量，用增加的方式处理。
10、--last-value 6：表示上一次的最后一个值是到几。
导入的增量部分在一个新的文件中
sqoop job --list  查看都有哪些job
sqoop job --exec myjob 执行job
完整的脚本，已经验证过
sqoop import \
--connect jdbc:mysql://192.168.1.101:3306/etlmonitor \
--username root \
--password root  -m 1 \
--table etl_job_log \
--fields-terminated-by ',' \
--hive-import \
--hive-overwrite \
--hive-table dw.etl_job_log
--null-string '**'

Hive数据直接导入Mysql
sqoop export \
--connect jdbc:mysql://192.168.1.101:3306/etlmonitor \
--username root \
--password root  -m 1 \
--table etl_job_log \
--fields-terminated-by ',' \
--hive-export \
--hive-table dw.etl_job_log



将MySQL的etl_job_loc表结构复制到Hive的dw库中，表名为etl_job_loc
sqoop create-hive-table \
--connect jdbc:mysql://192.168.1.101:3306/etlmonitor \
--table etl_job_loc \
--username root \
--password root \
--fields-terminated-by '\t' \
--hive-table dw.etl_job_loc

# 追加数据
sqoop import \
--connect jdbc:mysql://192.168.1.101:3306/etlmonitor \
--username root \
--password root \
--table etl_job_loc \
--hive-import \
--hive-table dw.etl_job_loc
--fields-terminated-by '\t'
# 覆盖数据
sqoop import \
--connect jdbc:mysql://192.168.1.101:3306/etlmonitor \
--username root \
--password root \
--table  etl_job_loc \
--hive-import \
--hive-overwrite \
--hive-table dw.etl_job_loc \
--fields-terminated-by '\t'
注：如果MySQL中的表没有主键，则需要加--autoreset-to-one-mapper参数

#将hive表的数据导入到mysql中[已经验证]
sqoop export \
--connect jdbc:mysql://192.168.1.101:3306/etlmonitor \
--username root \
--password root \
--table etl_job_loc \
--columns "id,LOC_NM,LOC_CAP,CUR_WRKLD" \
--export-dir /user/hive/warehouse/dw.db/etl_job_loc \
--input-fields-terminated-by '\t'

