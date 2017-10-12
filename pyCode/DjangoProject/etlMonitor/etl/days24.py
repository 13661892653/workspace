#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
from django.shortcuts import render,redirect,HttpResponse
from django import forms
from django.forms import fields
from etl import models

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