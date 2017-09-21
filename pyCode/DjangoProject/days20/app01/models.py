from django.db import models

# Create your models here.
class Business(models.Model):
    caption=models.CharField(max_length=32)


class Host(models.Model):
    nid=models.AutoField(primary_key=True)
    hostname=models.CharField(max_length=32,db_index=True)
    ip=models.GenericIPAddressField(db_index=True)
    port=models.IntegerField()
    bussid=models.ForeignKey(to="Business",to_field='id')

class App(models.Model):
    r_host_app=models.ManyToManyField("Host")
    name=models.CharField(max_length=128)
