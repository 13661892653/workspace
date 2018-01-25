#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
__date__ = '2018/1/24 15:57'
__author__ = "Colby"
import urllib.request
import json
import re
from  lxml import etree
# def getGTChallenge(session):
#     loginurl="http://www.gsxt.gov.cn/SearchItemCaptcha"
#     result=session.get(loginurl)
#     mycookies= result.cookies
#     resp=result.text
#     resp=resp[8:]
#     tmp=resp.split('</script')
#     resp=tmp[0]
#     resp=resp.replace("eval(y.replace", "var aaa=(y.replace");
#     resp = resp + "aaa=aaa.replace(\"while(window._phantom||window.__phantomas){};\", \"\");bbb = aaa.split(\"setTimeout\");aaa = bbb[0] + \"return dc;}\";aaa = aaa.replace(\"var l=\", \"\");";
#     ctxt = PyV8.JSContext()
#     ctxt.enter()
#     func = ctxt.eval(resp)
#     fu=ctxt.eval("("+func+")")
#     jslarr= fu().split("=")
#     jsl_clearance=jslarr[1]
#     session.cookies['__jsl_clearance']=jsl_clearance
#     result=session.get(loginurl)
#     print(result.text)
#     challengeJson=json.loads(result.text)
#     return  challengeJson

def getUrl(url):
    headers ={
    'Accept':'*/*',
    #'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': '__jsluid=1cad96e66e70f8e27c4e6df45d34edd3; UM_distinctid=15f90ba9906814-0dcb89c99581c1-1e187f58-1fa400-15f90ba9907b48; tlb_cookie=S172.16.12.42; __jsl_clearance=1516865992.414|0|eJ7puGoh8IapVdRGZZhwHilf0zU%3D; gsxtBrowseHistory1=%0FS%04%06%1D%04%1D%10SNS%24%26%3B%22%3D%3A71%3A%3B01%3A%219GGDDDDGGDDDDDDDDDECELFSXS%11%1A%00%1A%15%19%11SNS%E6%B4%AD%E6%B0%AB%E7%BA%9D%E4%B9%84%E5%B3%9D%E5%9D%AB%E6%8B%B4%E6%9D%9B%E8%83%95%E4%BA%89%E6%9D%BD%E9%98%A4%E5%84%98%E5%8E%8CSXS%11%1A%00%00%0D%04%11SNEFFMXS%02%1D%07%1D%00%00%1D%19%11SNEAEA%40DCMLMBDE%09; gsxtBrowseHistory2=%0FS%04%06%1D%04%1D%10SNS%24%26%3B%22%3D%3A71%3A%3B01%3A%219%40FDDDDEBDDDDDDFLLMMGG%40MLSXS%11%1A%00%1A%15%19%11SNS%E8%BE%9E%E6%98%9A%E8%B4%96%E6%81%A9%E7%A6%A5%E6%8B%B4%EF%BD%BC%E6%AC%92%E6%B0%BD%EF%BD%BD%E6%9D%BD%E9%98%A4%E5%84%98%E5%8E%8CSXS%11%1A%00%00%0D%04%11SNEEGDXS%02%1D%07%1D%00%00%1D%19%11SNEAEAGCCFLEMLD%09; gsxtBrowseHistory3=%0FS%04%06%1D%04%1D%10SNS%24%26%3B%22%3D%3A71%3A%3B01%3A%219GEDDDDGEDEEDDDDDFFDEEDGEADDD%40MSXS%11%1A%00%1A%15%19%11SNS%E4%B9%BE%E6%B4%83%E4%BE%95%E9%9B%B2%E8%A0%B8%E4%BE%95%E6%80%9B%E7%A6%A5%E6%8B%B4%E8%83%95%E4%BA%89%E6%9D%BD%E9%98%A4%E5%84%98%E5%8E%8CSXS%11%1A%00%00%0D%04%11SNEFFFXS%02%1D%07%1D%00%00%1D%19%11SNEAEBLBLMFCGEB%09; CNZZDATA1261033118=443484846-1509960630-null%7C1516864316; Hm_lvt_cdb4bc83287f8c1282df45ed61c4eac9=1516777013,1516777780,1516788361,1516848578; Hm_lpvt_cdb4bc83287f8c1282df45ed61c4eac9=1516868923; JSESSIONID=8CAFD16E7DA816B1E7716D84781A78EC-n1:2',
    'Host': 'www.gsxt.gov.cn',
    'Upgrade - Insecure - Requests': '1',
    'Referer': 'http://www.gsxt.gov.cn/%7BW2JO46AgerT0-_BM-RvdKKUikfuwt-cLV0wkPRzr4RdzC3fy3rmhHdh-jng7OJk8RlMkBQn-lJJcQhKMp0KFHsz9THSebHs0brMs_-B7QsyofHh4kxVdtpCwJV6md1dGsCmc727NIi0bZytAMo82LiN3lddozF2lOosQQwkON6Y-1516852920035%7D',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3018.3 Safari/537.36'
    }
    req = urllib.request.Request(url=url, headers=headers)
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    return html

if __name__=="__main__":
    print("script init...")
    print("当前等待爬取的企业数...")
    url="http://www.gsxt.gov.cn/%7BW2JO46AgerT0-_BM-RvdKKUikfuwt-cLV0wkPRzr4RdzC3fy3rmhHdh-jng7OJk8RlMkBQn-lJJcQhKMp0KFHsz9THSebHs0brMs_-B7QsyofHh4kxVdtpCwJV6md1dGsCmc727NIi0bZytAMo82LiN3lddozF2lOosQQwkON6Y-1516852920035%7D"
    #url='http://www.easyrong.com'
    html=getUrl(url)
    selector = etree.HTML(html)
    统一社会信用代码= selector.xpath('//*[@id="primaryInfo"]/div/div[2]/dl[1]/dd/text()')[0]
    企业名称= selector.xpath('//*[@id="primaryInfo"]/div/div[2]/dl[2]/dd/text()')[0]
    类型= selector.xpath('//*[@id="primaryInfo"]/div/div[2]/dl[3]/dd/text()')[0]
    法定代表人      = selector.xpath('//*[@id="primaryInfo"]/div/div[2]/dl[4]/dd/text()')[0]
    注册资本 = selector.xpath('//*[@id="primaryInfo"]/div/div[2]/dl[5]/dd/text()')[0]
    成立日期 = selector.xpath('//*[@id="primaryInfo"]/div/div[2]/dl[6]/dd/text()')[0]
    营业期限自 = selector.xpath('//*[@id="primaryInfo"]/div/div[2]/dl[7]/dd/text()')[0]
    营业期限至 = selector.xpath('//*[@id="primaryInfo"]/div/div[2]/dl[8]/dd/text()')[0]
    登记机关 = selector.xpath('//*[@id="primaryInfo"]/div/div[2]/dl[9]/dd/text()')[0]
    核准日期 = selector.xpath('//*[@id="primaryInfo"]/div/div[2]/dl[10]/dd/text()')[0]
    登记状态 = selector.xpath('//*[@id="primaryInfo"]/div/div[2]/dl[11]/dd/text()')[0]
    住所 = selector.xpath('//*[@id="primaryInfo"]/div/div[2]/dl[12]/dd/text()')[0]
    经营范围 = selector.xpath('//*[@id="primaryInfo"]/div/div[2]/dl[13]/dd/text()')[0]
    '//*[@id="primaryInfo"]/div/div[2]/dl[3]/dd'
    print(re.sub("\D", "", 统一社会信用代码))
    print(企业名称)
    print(类型)
    print(法定代表人)
    print(注册资本)
    print(成立日期)
    print(营业期限自)
    print(营业期限至)
    print(登记机关)
    print(核准日期)
    print(登记状态)
    print(住所)
    print(经营范围)
