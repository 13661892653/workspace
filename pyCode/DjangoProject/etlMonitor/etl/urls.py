#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
__author__ = 'colby'
from django.conf.urls import url,include
from etl import views
from etl import logins
urlpatterns = [
    #登录注册logins
    url(r'^register/', logins.register),
    url(r'^login/', logins.login),
    #作业日志查看
    url(r'^queryjob/(?P<pid>\d*)', views.queryjob),
    url(r'^testpage/', views.testpage),
    url(r'^index_detail-delete-(?P<nid>\d+)', views.detail_delete),
    url(r'^index_detail-update-(?P<nid>\d+)', views.detail_update),
]