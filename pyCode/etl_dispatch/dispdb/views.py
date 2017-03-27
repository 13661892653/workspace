#coding=utf-8
from django.shortcuts import render
from dispdb import models
from dispdb import comm
from dispdb import html_helper

def index(request):
    return render(request,'index.html')
def test(request):
    return render(request, 'jobInfo.html')
def jobquery(request):
    return render(request, 'jobInfo.html')

# Create your views here.
def dbinfo(request,page):
    user_list = []
    areaname = request.POST.get("areaname", '')
    databasename = request.POST.get("databasename", '')
    tablename_ch = request.POST.get("tablename_ch", '')
    tablename_en = request.POST.get("tablename_en", '')
    columnname_ch = request.POST.get("columnname_ch", '')
    columnname_en = request.POST.get("columnname_en", '')
    #print(areaname,databasename,tablename_ch,tablename_en,columnname_ch,columnname_en)
    count=0
    page_string=''
    per_item = comm.try_int(request.COOKIES.get('pager_num', 20), 10)
    if request.method == "POST":
        global count
        global page_string
        global per_item
        per_item = comm.try_int(request.COOKIES.get('pager_num', 20), 10)
        page = comm.try_int(page, 1)
        count =      models.dbinfo.objects.filter(domainname__contains=areaname).filter(tableschema__contains=databasename).filter(tablename__contains=tablename_en).filter(tabledesc__contains=tablename_ch).filter(columnname__contains=columnname_en).filter(columndesc__contains=columnname_ch).count()
        #print('数据总数',count)
        pageObj = html_helper.PageInfo(page, count, per_item)
        print('start',pageObj.start,'end',pageObj.end)
        user_list =  models.dbinfo.objects.filter(domainname__contains=areaname).filter(tableschema__contains=databasename).filter(tablename__contains=tablename_en).filter(tabledesc__contains=tablename_ch).filter(columnname__contains=columnname_en).filter(columndesc__contains=columnname_ch)[pageObj.start:pageObj.end]
        page_string = html_helper.pager(page, pageObj.all_page_count)
        print(page,pageObj.all_page_count)
        pagecnt = pageObj.all_page_count
        response = render(request, "dbinfo.html",
                          {'data': user_list, 're_areaname': areaname, 'databasename': databasename,
                           'tablename_ch': tablename_ch, 'tablename_en': tablename_en, 'columnname_ch': columnname_ch,
                           'columnname_en': columnname_en, 'count': count, 'page': page_string, 'pagecnt': pagecnt})
        response.set_cookie('pager_num', per_item)
    else:
        global count
        global page_string
        global per_item
        per_item = comm.try_int(request.COOKIES.get('pager_num', 20), 10)
        page = comm.try_int(page, 1)
        count = models.dbinfo.objects.filter(domainname__contains=areaname).filter(
            tableschema__contains=databasename).filter(tablename__contains=tablename_en).filter(
            tabledesc__contains=tablename_ch).filter(columnname__contains=columnname_en).filter(
            columndesc__contains=columnname_ch).count()
        #print('数据总数', count)
        pageObj = html_helper.PageInfo(page, count, per_item)
        print('start', pageObj.start, 'end', pageObj.end)
        user_list = models.dbinfo.objects.filter(domainname__contains=areaname).filter(
            tableschema__contains=databasename).filter(tablename__contains=tablename_en).filter(
            tabledesc__contains=tablename_ch).filter(columnname__contains=columnname_en).filter(
            columndesc__contains=columnname_ch)[pageObj.start:pageObj.end]
        page_string = html_helper.pager(page, pageObj.all_page_count)
        print(page, pageObj.all_page_count)
        pagecnt=pageObj.all_page_count
        response = render(request, "dbinfo.html",
                          {'data': user_list, 're_areaname': areaname, 'databasename': databasename,
                           'tablename_ch': tablename_ch, 'tablename_en': tablename_en, 'columnname_ch': columnname_ch,
                           'columnname_en': columnname_en, 'count': count, 'page': page_string, 'pagecnt': pagecnt})
        response.set_cookie('pager_num', per_item)
    return response