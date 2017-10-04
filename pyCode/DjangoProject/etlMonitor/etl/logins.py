#coding=utf-8
#PythonVer:3.5.2
__Author__='colby chen'
from django.shortcuts import render,redirect,HttpResponse
from django import forms
from django.forms import widgets
from django.forms import fields
from etl import models
import datetime,time
class FormVal(forms.Form):
    username=fields.CharField(error_messages={'required':'用户名不能为空'},
                              widget=widgets.TextInput(attrs={'id': 'username'}))
    password1 = fields.CharField(max_length=16,
                                 min_length=6,
                                 error_messages={'required':'密码不能为空',
                                                 'max_length':'密码最大长度不能超过16',
                                                 'min_length': '密码最小长度为6位'},
                                 widget=widgets.PasswordInput(attrs={'id': 'password1'}))
    password2 = fields.CharField(error_messages={'required':'密码不能为空'},
                                 widget=widgets.PasswordInput(attrs={'id': 'password2'}))
    email = fields.EmailField(error_messages={'required':'邮箱不能为空'},
                              widget=widgets.TextInput(attrs={'id': 'email'}))
    mobile = fields.CharField(error_messages={'required':'手机号不能为空',
                                              'invalid':'邮箱格式错误'},
                              widget=widgets.TextInput(attrs={'id': 'mobile'}))

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        iscookie=request.POST.get('iscookie')
        print(username,password,iscookie)
        loginResult=models.USER.objects.filter(USERNAME=username,PASSWORD=password).first()
        print(loginResult)
        if loginResult:
            request.session['username'] = username
            request.session['is_login'] = True
            if request.POST.get('iscookie', None) == '1':
                request.session.set_expiry(1209600)
            return redirect('/etl/queryjob')
        else:
            message='用户或密码错误'
            return render(request, 'login.html', {'message': message})

def register(request):
    if request.method == "GET":
        # 从数据库中吧数据获取到
        # username=request.GET.get('username')
        # password = request.GET.get('password')
        # email = request.GET.get('email')
        # mobile = request.GET.get('mobile')
        # dic = {
        #     "USERNAME": username,
        #     'PASSWORD': password,
        #     'EMAIL': email,
        #     'MOBILE': mobile
        # }
        obj = FormVal()
        #print(dic)
        return render(request, 'register.html', {'obj': obj})
    elif request.method == "POST":
        # 获取用户所有数据
        # 每条数据请求的验证
        # 成功：获取所有的正确的信息
        # 失败：显示错误信息
        obj = FormVal(request.POST)
        r1 = obj.is_valid()
        print(r1)
        if r1:
            # obj.cleaned_data
            #print(obj.cleaned_data)
            checkUser=models.USER.objects.filter(USERNAME=obj.cleaned_data['username'])
            if checkUser:
                message='用户已经存在！'
                return render(request, 'register.html', {'obj': obj,'message':message})
            else:
                message='注册成功！'
                models.USER.objects.create(USERNAME=obj.cleaned_data['username'],
                                           PASSWORD=obj.cleaned_data['password2'],
                                           EMAIL=obj.cleaned_data['email'],
                                           MOBILE =obj.cleaned_data['mobile'],
                                           REG_DATE=time.time(),
                                           LOGIN_DATE=time.time()
                                           )
                return render(request, 'register.html', {'message': message})
        else:
            # ErrorDict
            # print(obj.errors.as_json())
            # print(obj.errors['user'][0])通过字典取数据
            #print(obj.errors)
            return render(request, 'register.html', {'obj': obj})
        return render(request, 'register.html')