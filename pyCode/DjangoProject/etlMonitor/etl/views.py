from django.shortcuts import render
import time
# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from etl import models
def index(request):
    if request.method=='GET':
        return render(request, 'index.html')
    elif request.method=='POST':
        job_id = request.POST.get('job_id')
        job_name = request.POST.get('job_name')
        job_type = request.POST.get('job_type')
        job_status = request.POST.getlist('job_status')[0]
        data_prd_st = request.POST.get('data_prd_st')
        data_prd_ed = request.POST.get('data_prd_ed')
        if data_prd_st == '':
            data_prd_st='0000-01-01'
        if data_prd_ed == '':
            data_prd_ed='2099-01-01'

        obj=models.JOB_LOG.objects.filter(JOB_SEQ_ID__contains=job_id,
                                          JOB_NM__contains=job_name,
                                          #JOB_TYPE=job_type,
                                          JOB_STS=job_status,
                                          DATA_PRD__gt=data_prd_st,
                                          DATA_PRD__lt=data_prd_ed
                                          )
        record=obj.count()
        print('obj',obj,'record',record)
        return render(request, 'index.html',{'data':obj,'record':record})
def login(request):
    pass