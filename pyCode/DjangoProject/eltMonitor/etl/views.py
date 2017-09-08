from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    username=request.POST.get('username')
    password = request.POST.get('password')
    if username=='colby' and password=='123':
        return render(request,'login.html')
    else:
        msg='用户名或者密码错误'
    return render(request,'index.html',{'msg':msg})

def login(request):
    pass