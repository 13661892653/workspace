#coding=utf-8
from django.shortcuts import render,HttpResponse,redirect
from django.core import serializers
import json
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


def app(request):
    ret = {'status': True, 'error': None, 'data': None}
    if request.method=='GET':
        data_app=models.App.objects.all()
        data_host = models.Host.objects.all()
        return render(request, 'app.html', {'data_app': data_app,'data_host':data_host})
    elif request.method=='POST':
        # try:
        #     obj = models.App.objects.all()
        #     ret['data']=obj
        #     print('11111111111111111', type(ret))
        #     ret=serializers.serialize("json", ret)
        # except Exception as e:
        #     ret['status'] = False
        #     ret['error'] = '请求错误'
        # return HttpResponse(json.dumps(ret),content_type='application/json')
        appname=request.POST.get('appname')
        hostname=request.POST.getlist('hostname')
        print(appname,hostname)
        obj=models.App.objects.create(name=appname)
        obj.r_host_app.add(*hostname)
        return redirect('/app')
    else:
        pass


def app_ajax(request):
    if request.method == 'POST':
        ret = {'status': True, 'error': None, 'data': None}
        appname = request.POST.get('appname')
        hostname = request.POST.getlist('hostname')
        print('打印输出',appname, hostname)
        obj = models.App.objects.create(name=appname)
        obj.r_host_app.add(*hostname)
        return HttpResponse(json.dumps(ret))
    else:
        pass