#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
__date__ = '2017/12/27 15:06'
__author__ = "Colby"
import xadmin
from xadmin import views
from .models import EmailVerifyRecord,Banner

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class GlobalSettings(object):
    site_title="--信隆行数据调度系统--"
    site_footer="上海信隆行信息科技股份有限公司"
    menu_style="accordion"

class EmailVerifyRecordAdmin(object):
    # 增删改
    list_display=['code','email','send_type','send_time']
    # 查找
    search_fields = ['code', 'email', 'send_type']
    # 筛选
    list_filter = ['code','email','send_type','send_time']

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index','add_time']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)