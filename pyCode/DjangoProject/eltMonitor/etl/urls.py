#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
__author__ = 'colby'
from django.conf.urls import url,include
from etl import views
urlpatterns = [
    url(r'^index/', views.index),
]