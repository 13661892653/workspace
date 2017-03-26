#coding=utf-8
from django.db import models

# Create your models here.
#作业基本信息表
class jobinfo(models.Model):
    '''
    JOB名称、JOB类型、JOB路径、运行命令、调度周期
    JOB优先级、JOB有效性、负责人、插入时间、更新时间
    '''
    job_name = models.CharField(max_length=128)
    job_type = models.CharField(max_length=128)
    job_path = models.CharField(max_length=128)
    job_comm = models.CharField(max_length=1024)
    job_rate = models.CharField(max_length=10)
    job_priority = models.CharField(max_length=10)
    job_valid = models.CharField(max_length=6)
    create_person= models.CharField(max_length=64)
    insert_date = models.DateField(max_length=26)
    update_date = models.DateField(max_length=26)

#作业依赖表
class jobsequence(models.Model):
    '''
    作业ID、作业名称、前一作业ID、前一作业名称、插入时间、更新时间
    '''
    job_name=models.CharField(max_length=128)
    pre_job_name=models.CharField(max_length=128)
    insert_date = models.DateField(max_length=26)
    update_date = models.DateField(max_length=26)
#作业运行表
class jobrun(models.Model):
    '''
    时间批次、作业名称、作业运行状态、调度周期、负责人、
    开始时间、结束时间、错误次数、日志路径、插入时间、更新时间
    '''
    date_batch =models.DateField(max_length=26)
    job_name=models.CharField(max_length=128)
    job_status = models.CharField(max_length=10)
    job_rate = models.CharField(max_length=10)
    create_person = models.CharField(max_length=64)
    start_date = models.DateField(max_length=26)
    end_date = models.DateField(max_length=26)
    error_count=models.CharField(max_length=26)
    log_path=models.CharField(max_length=512)
    insert_date = models.DateField(max_length=26)
    update_date = models.DateField(max_length=26)
#数据库基本信息表
class dbinfo(models.Model):
    domainname=models.CharField(max_length=32)
    tableschema=models.CharField(max_length=128)
    tablename=models.CharField(max_length=128)
    tabledesc=models.CharField(max_length=1024)
    columnname=models.CharField(max_length=128)
    columndesc=models.CharField(max_length=1024)
    datatype=models.CharField(max_length=64)
    columntype=models.CharField(max_length=64)

#ETL关系映射表
