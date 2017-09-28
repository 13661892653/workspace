#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
'''
drop table youboy_diqu;
drop table youboy_enterprise;
CREATE TABLE
    youboy_diqu
    (
        provinceName VARCHAR(50) NOT NULL COMMENT '省份',
        cityName VARCHAR(50) NOT NULL COMMENT '市区',
        url VARCHAR(255) COMMENT 'url地址',
        flag VARCHAR(1),
        PRIMARY KEY (provinceName, cityName)
    )
    ENGINE=InnoDB DEFAULT CHARSET=utf8;
    
CREATE TABLE youboy_enterprise
    (
        provinceName VARCHAR(50) comment '省份、直辖市、自治区',
        cityName VARCHAR(50) comment '市、自治州',
        catagory_1_Name VARCHAR(50) comment '一级类目url',
        catagory_1_Url VARCHAR(50) comment '一级类目名称',
        catagory_2_Name VARCHAR(50) comment '二级类目名称',
        catagory_2_Url VARCHAR(50) comment '二级类目url',
        catagory_3_Name VARCHAR(50) comment '三级类目名称',
        catagory_3_Url VARCHAR(50) comment '三级类目url',
        enterpriseName VARCHAR(125) comment '企业名称',
        contactPerson VARCHAR(50) comment '企业联系人',
        enterpriseFax VARCHAR(50) comment '企业传真',
        enterprisePhone VARCHAR(50) comment '企业电话',
        enterpriseMobile VARCHAR(50) comment '企业手机',
        enterpriseAddr VARCHAR(255) comment '企业联系地址'
    )
    ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''