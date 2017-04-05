#coding=utf-8
'''通过cookie模拟登陆新浪微博'''
import requests
from  lxml import etree
from multiprocessing.dummy import Pool
cook1={"Cookie":" SINAGLOBAL=9856325689160.768.1483514635632; login_sid_t=f1835519aba1d5e62a9c9628ac88c6ea; TC-Ugrow-G0=370f21725a3b0b57d0baaf8dd6f16a18; TC-V5-G0=1e4d14527a0d458a29b1435fb7d41cc3; _s_tentry=www.baidu.com; Apache=8102206826604.998.1491373984971; ULV=1491373984976:7:1:1:8102206826604.998.1491373984971:1488941755147; appkey=; TC-Page-G0=4c4b51307dd4a2e262171871fe64f295; WBStorage=02e13baf68409715|undefined; UOR=,,login.sina.com.cn; SCF=AqIBKafr4dozVI0J3aQYrV5UiA5U1WWcqm-te9z2MUHkx0w-r9eOrZ_b4LT-c7wX7JD_PfyV06ZWD3kTu5QIf1E.; SUB=_2A2514OlADeRhGeNH7FMX-SnLyjqIHXVWlF2IrDV8PUNbmtAKLXD-kW8dHAeAP_AFTxY23byEGHmDzEHRVA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhVd8JS0vKbseyG4Fl9e44h5JpX5K2hUgL.Fo-4S02c1KMNeKq2dJLoIEWodcpbwCH8SE-4BC-RSFH81CHW1CHWBEH8SE-4SFHFentt; SUHB=0auwl4IxIsa5lg; ALF=1522912399; SSOLoginState=1491376400; un=13661892653; wvr=6; WBtopGlobal_register_version=d55ace0a0a9bdd99"}
cook2={"Cookie":" SINAGLOBAL=9856325689160.768.1483514635632; d5e62a9c9628ac88c6ea; TC-Ugrow-G0=370f21725a3b0b57d0baaf8dd6f16a18; TC-V5-G0=1e4d14527a0d458a29b1435fb7d41cc3; _s_tentry=www.baidu.com; Apache=8102206826604.998.1491373984971; ULV=1491373984976:7:1:1:8102206826604.998.1491373984971:1488941755147; appkey=; TC-Page-G0=4c4b51307dd4a2e262171871fe64f295; WBStorage=02e13baf68409715|undefined; UOR=,,login.sina.com.cn; SCF=AqIBKafr4dozVI0J3aQYrV5UiA5U1WWcqm-te9z2MUHkx0w-r9eOrZ_b4LT-c7wX7JD_PfyV06ZWD3kTu5QIf1E.; SUB=_2A2514OlADeRhGeNH7FMX-SnLyjqIHXVWlF2IrDV8PUNbmtAKLXD-kW8dHAeAP_AFTxY23byEGHmDzEHRVA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhVd8JS0vKbseyG4Fl9e44h5JpX5K2hUgL.Fo-4S02c1KMNeKq2dJLoIEWodcpbwCH8SE-4BC-RSFH81CHW1CHWBEH8SE-4SFHFentt; SUHB=0auwl4IxIsa5lg; ALF=ginState=1491376400; un=13661892653; wvr=6; WBtopGlobal_register_version=d55ace0a0a9bdd99"}
url="http://weibo.com/u/5971697716/home?wvr=5"
html1=requests.get(url).content
html2=requests.get(url,cookies=cook1).content
html3=requests.get(url,cookies=cook2).content
#不带cookie
print(html1)
#带正确的cookie
print(html2)
#带错误的cookie
print(html3)