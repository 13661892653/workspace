from django.shortcuts import render
import time
# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
from etl import models

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        job_seq_id = request.POST.get('job_seq_id')
        job_name = request.POST.get('job_name')
        job_type = request.POST.get('job_type')
        job_status = request.POST.getlist('job_status')[0]
        data_prd_st = request.POST.get('data_prd_st')
        data_prd_ed = request.POST.get('data_prd_ed')
        if data_prd_st == '':
            data_prd_st = '0000-01-01'
        if data_prd_ed == '':
            data_prd_ed = '2099-01-01'

        obj = models.JOB_LOG.objects.filter(JOB_SEQ_ID__contains=job_seq_id,
                                            JOB_NM__contains=job_name,
                                            # JOB_TYPE=job_type,
                                            JOB_STS__contains=job_status,
                                            DATA_PRD__gt=data_prd_st,
                                            DATA_PRD__lt=data_prd_ed
                                            )
        record = obj.count()
        # print('obj',obj,'record',record)
        return render(request, 'index.html', {'data': obj, 'record': record})


def detail_delete(request, nid):
    models.JOB_LOG.objects.filter(JOB_SEQ_ID=nid).delete()
    return redirect('/etl/index/')


def detail_update(request, nid):
    models.JOB_LOG.objects.filter(JOB_SEQ_ID=nid).update(JOB_STS='WAITING')
    return redirect('/etl/index/')


def testpage(request):
    data = []
    perSize = 10
    totalCount = 1000
    currentPage = request.GET.get('page', 1)
    currentPage = int(currentPage)
    for i in range(1, totalCount + 1):
        data.append(i)
    begin = (currentPage - 1) * perSize
    end = currentPage * perSize
    data = data[begin:end]

    totalPage, yushu = divmod(totalCount, perSize)
    if totalPage<11:
        firstPage = 1
        lastPage = totalPage
    else:
        if currentPage<=(perSize/2)+1:
            firstPage = 1
            lastPage=perSize+1
        if currentPage<=totalPage-(perSize/2)-1:
            firstPage = currentPage
            lastPage=totalPage
        else:
            firstPage = currentPage-5
            lastPage = currentPage + 5 + 1
    pageStr = []
    for j in range(firstPage, lastPage+1):
        tempStr = '<li><a href="/etl/testpage/?page=%s">%s</a></li>' % (j, j)
        pageStr.append(tempStr)
    pageStr = ''.join(pageStr)
    pageStr = mark_safe(pageStr)

    return render(request, 'testPage.html', {'data': data, 'pageStr': pageStr})
