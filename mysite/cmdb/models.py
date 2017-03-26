#coding=utf-8
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    UserInfo_user=models.CharField(max_length=128)
    UserInfo_pwd=models.CharField(max_length=128)

class Phone(models.Model):
    Phone_no=models.CharField(max_length=128)
    Phone_name=models.CharField(max_length=128)

class Area(models.Model):
    Area_id=models.CharField(max_length=128)
    Area_name=models.CharField(max_length=128)

class Org(models.Model):
    Org_id=models.CharField(max_length=128)
    Org_name=models.CharField(max_length=128)
class MET_ALL_COLUMNS(models.Model):
    IP=models.CharField(max_length=128)
    TABLE_SCHEMA=models.CharField(max_length=128)
    TABLE_NAME = models.CharField(max_length=128)
    TABLE_SCHEMA = models.CharField(max_length=128)
    TABLE_ROWS = models.CharField(max_length=128)
    TABLE_COMMENT = models.CharField(max_length=128)
    COLUMN_NAME = models.CharField(max_length=128)
    COLUMN_COMMENT = models.CharField(max_length=128)
    COLUMN_TYPE = models.CharField(max_length=128)
    IS_NULLABLE = models.CharField(max_length=128)
