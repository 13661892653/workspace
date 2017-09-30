#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
__author__ = 'colby'
from django.conf.urls import url,include
from etl import views
urlpatterns = [
    url(r'^index/', views.index),
    url(r'^testpage/', views.testpage),
    url(r'^index_detail-delete-(?P<nid>\d+)', views.detail_delete),
    url(r'^index_detail-update-(?P<nid>\d+)', views.detail_update),
]