#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
__author__ = 'colby'
import core
from core.dbDML import DML
#homeDir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append(homeDir)


def promtInfo(*args):
    # 功能列表展示
    funList = []
    #print(args[0])
    print('可操作权限>>')
    for i in args[0]:
        funList.append(args[0].index(i) + 1)
        print(args[0].index(i) + 1, i)
    data = input('请选择操作，输入功能编号%s即可:' % funList)
    return data


def login(user,password):
    # 登录密码验证
    login_db=DML()
    res=login_db.Query_User(user,password)
    if res==None:
        return 'False'
    else:
        print('已经登录成功...')
        roleView(res.role_id)

def roleView(roleid):
    #根据功能编号调用对应模块
    if roleid==1:
        role_student=['提交作业','查看作业成绩','查看作业排名']
        funNum=promtInfo(role_student)

    elif roleid==2:
        role_teacher = ['班级管理','学员管理','创建上课记录','批改作业']
        funNum = int(promtInfo(role_teacher))
        if funNum==1:
            role_21 = ['创建班级', '删除班级']
            funNum = promtInfo(role_21)
        elif funNum==2:
            role_22 = ['增加学员', '删除学员', '修改学员信息']
            funNum = promtInfo(role_22)
        elif funNum==3:
            pass
        elif funNum==4:
            pass
        else:
            print('编号错误，请重新输入！')
    else:
        print('角色错误！')
        pass
