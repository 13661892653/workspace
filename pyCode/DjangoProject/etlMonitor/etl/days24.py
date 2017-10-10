#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
from django.shortcuts import render,redirect,HttpResponse
__author__ = "Colby"
def days24(request):
    if request.method=='GET':
        return render(request,'days24.html')
    if request.method=='POST':
        pass