from django.db import models

# Create your models here.
class JOB_LOC(models.Model):
    LOC_NM=models.CharField(max_length=64)
    LOC_CAP=models.IntegerField()
    CUR_WRKLD=models.CharField(max_length=11)


class JOB_LOG(models.Model):
    JOB_SEQ_ID=models.AutoField(primary_key=True)
    JOB_STS=models.CharField(max_length=12)
    JOB_NM=models.CharField(max_length=128)
    DATA_PRD=models.CharField(max_length=10)
    ACT_ST_DT=models.CharField(max_length=10,null=True)
    ACT_ST_TM=models.CharField(max_length=8,null=True)
    ACT_ED_DT=models.CharField(max_length=10,null=True)
    ACT_ED_TM=models.CharField(max_length=8,null=True)
    JOB_LG=models.CharField(max_length=24,null=True)
    RW_RD=models.IntegerField(null=True)
    RW_IST=models.IntegerField(null=True)
    RW_UPT=models.IntegerField(null=True)


class JOB_METADATA(models.Model):
    JOB_ID = models.AutoField(primary_key=True)
    JOB_NM=models.CharField(max_length=128)
    SCHD_PERIOD=models.CharField(max_length=12)
    JOB_TP=models.CharField(max_length=15)
    LOCATION=models.CharField(max_length=255)
    JOBCMD=models.CharField(max_length=255)
    PARAMS=models.CharField(max_length=255)
    PRIORITY=models.CharField(max_length=255)
    EST_WRKLD=models.CharField(max_length=255)
    PLD_ST_DT=models.DateField()
    PLD_ST_TM=models.TimeField()
    EXP_ED_DT=models.DateField()
    EXP_ED_TM=models.TimeField()
    MTX_GRP=models.CharField(max_length=128)
    NTY_PTY=models.CharField(max_length=128)
    INIT_FLAG=models.CharField(max_length=2)
    PPN_TSTMP=models.CharField(max_length=128)


class JOB_SEQ(models.Model):
    SEQ_ID=models.AutoField(primary_key=True)
    JOB_NM=models.CharField(max_length=128)
    PRE_JOB=models.CharField(max_length=128)
    SEQ_TY=models.CharField(max_length=128)

class USER(models.Model):
    USERNAME=models.CharField(max_length=25)
    PASSWORD=models.CharField(max_length=16)
    EMAIL = models.CharField(max_length=64)
    MOBILE = models.CharField(max_length=11,default='00000000000')
    REG_DATE=models.CharField(max_length=30)
    LOGIN_DATE = models.CharField(max_length=30)

################################################
class UserType(models.Model):
    caption=models.CharField(max_length=32)


class UserInfo(models.Model):
    username=models.CharField(verbose_name='用户名',max_length=32)
    email=models.EmailField(verbose_name='邮箱')
    #usertype=models.ForeignKey(verbose_name='用户类型',to='UserType',to_field='id')