from django.shortcuts import render,redirect,render_to_response

# Create your views here.
def index(request):
    is_login=request.session.get("is_login",None)
    if not is_login:
        return render_to_response("app2/login.html")
    else:
        return render_to_response("app2/index.html")
def login(request):
    if request.method=="POST":
        user=request.POST.get("username",None)
        pwd = request.POST.get("password", None)
        if user=="chenlun" and pwd=="123":
            request.session["is_login"]=True
            return  redirect("/app2/index/")
        else:
            return render_to_response("app2/login.html", {"msg": "用户名或密码错误"})
    return render_to_response("app2/login.html")
