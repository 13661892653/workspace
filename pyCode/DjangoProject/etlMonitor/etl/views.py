#coding=utf-8
from django.shortcuts import render
import time
# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
from etl import models
from comm import paging

def job_query(request,pid):
    if request.session.get('is_login'):
        if request.method=='GET':
            pageCodeNum = 10
            currentPage = request.GET.get('page', 1)
            perSize = request.COOKIES.get("per_page_count", 20)
            perSize = int(perSize)
            currentPage = int(currentPage)
            if currentPage <= 0:
                currentPage = 1
            totalCount = models.JOB_LOG.objects.all().count()
            pageObj = paging.Page(currentPage, totalCount, perSize, pageCodeNum)
            data = models.JOB_LOG.objects.all()[pageObj.beginCount:pageObj.endCount]
            pageStr = pageObj.pageStr("/etl/job_query/")
            jobstatusList = models.JOB_LOC.objects.all()
            username=request.session.get('username')
            return render(request, 'job_query.html', {'data': data,
                                                     'record': totalCount,
                                                     'pageStr': pageStr,
                                                     'jobstatusList':jobstatusList,
                                                     'username':username
                                                      })
        if request.method=='POST':
            pageCodeNum = 10
            currentPage = request.GET.get('page', 1)
            perSize = request.COOKIES.get("per_page_count", 20)
            perSize = int(perSize)
            currentPage = int(currentPage)
            if currentPage <= 0:
                currentPage = 1
            job_seq_id = request.POST.get('job_seq_id')
            job_name = request.POST.get('job_name')
            job_status = request.POST.getlist('job_status')[0]
            data_prd_st = request.POST.get('data_prd_st')
            data_prd_ed = request.POST.get('data_prd_ed')
            if data_prd_st == '':
                data_prd_st = '0000-01-01'
            if data_prd_ed == '':
                data_prd_ed = '2099-01-01'
            jobstatusList = models.JOB_LOC.objects.all()
            print('job_status',job_status)
            if job_status=='ALL':
                job_status=''
            totalCount = models.JOB_LOG.objects.filter(JOB_SEQ_ID__contains=job_seq_id,
                                                JOB_NM__contains=job_name,
                                                JOB_STS__contains=job_status,
                                                DATA_PRD__gt=data_prd_st,
                                                DATA_PRD__lt=data_prd_ed
                                                ).count()
            pageObj = paging.Page(currentPage, totalCount, perSize, pageCodeNum)
            data = models.JOB_LOG.objects.filter(JOB_SEQ_ID__contains=job_seq_id,
                                                JOB_NM__contains=job_name,
                                                JOB_STS__contains=job_status,
                                                DATA_PRD__gt=data_prd_st,
                                                DATA_PRD__lt=data_prd_ed
                                                )[pageObj.beginCount:pageObj.endCount]
            pageStr = pageObj.pageStr("/etl/job_query/")
            username = request.session.get('username')
            return render(request, 'job_query.html', {'data': data,
                                                     'record': totalCount,
                                                     'pageStr': pageStr,
                                                     'jobstatusList': jobstatusList,
                                                     'username':username
                                                      })
    else:
        return redirect('/etl/login/')
def detail_delete(request, nid):
    models.JOB_LOG.objects.filter(JOB_SEQ_ID=nid).delete()
    return redirect('/etl/job_query/')


def detail_update(request, nid):
    models.JOB_LOG.objects.filter(JOB_SEQ_ID=nid).update(JOB_STS='WAITING')
    return redirect('/etl/job_query/')


def testpage(request):
    pageCodeNum=10
    totalCount = 1000
    currentPage = request.GET.get('page', 1)
    perSize = request.COOKIES.get("per_page_count",20)
    perSize=int(perSize)
    currentPage = int(currentPage)
    pageObj=paging.Page(currentPage, totalCount, perSize,pageCodeNum)
    data = []
    for i in range(1, totalCount + 1):
        data.append(i)
    data = data[pageObj.beginCount:pageObj.endCount]
    pageStr=pageObj.pageStr("/etl/testpage/")
    return render(request, 'testPage.html', {'data': data, 'pageStr': pageStr})
