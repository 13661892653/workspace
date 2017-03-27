from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.db import *
from cmdb import models
# Create your views here.
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
def index(request):
    pass
def Add(request,name):
    pass
def test5(request):
    return render(request, "test5.html", )
def Delete(request,name):
    pass
def Update(request,name):
    pass
def select(request):
    user_list=[]
    tabname=request.POST.get("tabname")
    if request.method=="POST":
        user_list=models.MET_ALL_COLUMNS.objects.filter(TABLE_NAME__contains=tabname)
        #cursor = connection.cursor()
        #cursor.execute('''SELECT * FROM MET_ALL_COLUMNS ''')
        #row = cursor.fetchone()
    return render(request,"index.html",{'data':user_list})
    #cursor = connection.cursor()
    #cursor.execute('''SELECT DISTINCT first_name ROM people_person WHERE last_name = %s''', ['Lennon'])
    #row = cursor.fetchone()
def metadata(request):
    return render(request, "metadata.html",)
def alert(request):
    return render(request, "test3.html",)
