#coding=utf-8
from django.shortcuts import render,render_to_response
from app1 import comm
from app1 import models
from app1 import html_helper
# Create your views here.
def index(request,page):
    #对传入的分页参数进行异常处理
    page=comm.try_int(page,1)
    #统计查询记录总数
    count = models.Host.objects.all().count()
    #获取分页开始页、结束页、页总数
    pageObj=html_helper.PageInfo(page,count)
    #返回查询结果集
    result=models.Host.objects.all()[pageObj.start:pageObj.end]
    #结果集返回一系列a标签字符，返回给前端用于动态分页
    page_string=html_helper.pager(page,pageObj.all_page_count)
    #以字典的形式返回给前端，包括结果集、记录总数、分页参数
    return render_to_response('index.html',{'data':result,'count':count,'page':page_string})
