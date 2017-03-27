#/usr/bin/python
#coding=utf-8
from django.shortcuts import render,redirect,render_to_response

# Create your views here.
from django.template import RequestContext,context


def index(request):
    #进入index页面，获取session值，将获取的值返回给前端页面
    user_dict=request.session.get("is_login",None)
    if user_dict:
        return render(request,"app2/index.html",{"user":user_dict['username'],"pwd":user_dict['password']})
    else:
        return render(request,"app2/login.html")
def login(request):
    if request.method=="POST":
        user=request.POST.get("username",None)
        pwd = request.POST.get("password", None)
        if user=="chenlun" and pwd=="123":
            #登录成功设置session
            request.session["is_login"]={"username":user,"password":pwd}
            return  redirect("/app2/index/")
        else:
            return render(request,"app2/login.html", {"msg": "用户名或密码错误"})
    return render(request,"app2/login.html")
def logout(request):
    #退出会话，删除session，返回登录页面
    del request.session['is_login']
    return render(request,"app2/login.html")