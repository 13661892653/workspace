#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
__author__ = 'colby'
from django.conf.urls import url,include
from etl import views
from etl import logins
from etl import days24
urlpatterns = [
    #登录注册logins
    url(r'^register/', logins.register),
    url(r'^login/', logins.login),
    url(r'^check_code.html', logins.checkCodeV),

    #作业日志查看
    url(r'^job_query/(?P<pid>\d*)', views.job_query),
    url(r'^testpage/', views.testpage),
    url(r'^index_detail-delete-(?P<nid>\d+)', views.detail_delete),
    url(r'^index_detail-update-(?P<nid>\d+)', views.detail_update),
    url(r'^days24/', days24.days24),
    url(r'^upload/', days24.upload),
    url(r'^upload_file/', days24.upload_file),
    #测试
    url(r'^iframetest/', days24.iframetest),
]