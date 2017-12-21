#coding="utf-8"
from django.db import models
from datetime import datetime
# Create your models here.
from django.contrib.auth.models import AbstractUser

#superuser:admin password:rootroot
#
class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=50,verbose_name="昵称",default=0)
    birday=models.DateField(verbose_name="生日",null=True,blank=True)
    gender=models.CharField(max_length=8,choices=(("male","男"),("female","女")),default="female")
    address=models.CharField(max_length=100,verbose_name="地址",default="")
    mobile = models.CharField(max_length=11, null=True,verbose_name="手机号", default="")
    image = models.ImageField(upload_to="image/%Y/%m",default="image/default.png",max_length=100)

    class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.username

class EmailVerifyRecord(models.Model):
    code=models.CharField(max_length=20,verbose_name="验证码")
    email=models.EmailField(max_length=50,verbose_name="邮箱")
    send_type=models.CharField(max_length=10,choices=(("register","注册"),("forget","找回密码")))
    send_time=models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

class Banner(models.Model):
    title=models.CharField(max_length=100,verbose_name="标题")
    image=models.ImageField(upload_to="banner/%Y/%m",verbose_name="轮播图")
    url=models.URLField(max_length=200,verbose_name="访问地址")
    index=models.IntegerField(default=100,verbose_name="序号")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name="轮播图"
        verbose_name_plural=verbose_name

