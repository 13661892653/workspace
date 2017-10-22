#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
from django.shortcuts import render,redirect,HttpResponse
from django import forms
from django.forms import fields
from etl import models
import json
import os
class UserInfoModelForm(forms.ModelForm):

    class Meta:
        model=models.UserInfo
        #fields=['username','email'] #只列出指定字段的名称
        #fields=['username','email'] #只列出指定字段的名称
        #exclude=['username','email'] #排除指定字段
        fields='__all__'

class UserInfoForm(forms.Form):
    username = fields.CharField(max_length=32)
    email = fields.EmailField()
    userType = fields.ChoiceField(
        choices=models.UserType.objects.values_list('id','caption')
    )
    def __init__(self,*args,**kwargs):
        super(UserInfoForm,self).__init__(*args,**kwargs)
        self.fields['userType'].choices=models.UserType.objects.values_list('id','caption')

def days24(request):
    if request.method=='GET':
        obj=UserInfoModelForm()
        return render(request,'days24.html',{'obj':obj})
    elif request.method=='POST':
        obj=UserInfoModelForm(request.POST)
        obj.is_valid()
        obj.errors
        return render(request, 'days24.html', {'obj': obj})
def iframetest(request):
    username=request.POST.get('username')
    email = request.POST.get('email')
    print(username,email)
    return render(request,'iframetest.html')

def upload(request):
    '''
    上传页面载入
    :param request:
    :return:
    '''
    return render(request,'upload.html')

def upload_file(request):
    '''
    文件上传处理
    :param request:
    :return:
    '''
    fileobj=request.FILES.get('sendFile')
    print(type(fileobj))
    imagePath=os.path.join('static/upload/',fileobj.name)
    print('imagePath',imagePath)
    #指定文件的上传路径
    with open(imagePath,'wb') as f:
        for item in fileobj.chunks():
            f.write(item)
    ret={'code':True,'data':imagePath}
    return HttpResponse(json.dumps(ret))