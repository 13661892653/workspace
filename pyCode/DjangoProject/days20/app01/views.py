from django.shortcuts import render
from app01 import models
# Create your views here.
def business(request):
    #data1结果集对象
    data1 = models.Business.objects.all()
    #data2返回的字典
    data2 = models.Business.objects.all().values('id','caption')
    #data3返回的列表
    data3 = models.Business.objects.all().values_list('id','caption')
    return render(request,'business.html',{'data1':data1,'data2':data2,'data3':data3})
def host(request):
    data1=models.Host.objects.all()
    return render(request, 'host.html', {'data1': data1})
