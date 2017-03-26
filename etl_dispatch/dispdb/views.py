from django.shortcuts import render,render_to_response
from django.db import *
from dispdb import models
from django.http import HttpResponseRedirect

def index(request):
    return render(request,'index.html')
# Create your views here.
def Jobquery(request):
    pass
def dbinfo(request):
    user_list=[]
    user_list=models.dbinfo.objects.all()
    return render(request,"dbinfo.html",{'data':user_list})