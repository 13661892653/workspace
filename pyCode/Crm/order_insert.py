#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin
import time
data={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'UM_distinctid=15f2965a717455-0ecb53f987d1c2-1e187f58-1fa400-15f2965a718550; __utmz=67240965.1523339484.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=67240965.818229032.1523339484.1523339484.1523347207.2; SESSION=eaa9c115-facd-4b58-8bc5-b8f8a14fbc8d',
    'Host': 'crm.easyrong.com',
    'Referer': 'http://crm.easyrong.com/login',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36'
}
def insert_content(browser,enterprise_name):
    print('当前采编的企业名称：',enterprise_name)
    enterpriseName = browser.find_element_by_id('enterpriseName')
    enterpriseName.send_keys(enterprise_name)
    #check_enterprise_name = browser.find_element_by_class_name('btn blue')
    #企业名称
    check_enterprise_name = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#corpOrder1 > div > input')))
    check_enterprise_name.click()

    #下单时间
    orderDate = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#orderDate')))
    orderDate.send_keys('2018-04-16 00:00:00')
    #采购商品

    # 采购单价
    orderPrice = browser.find_element_by_name('orderPrice')
    orderPrice.send_keys('160')
    # 采购数量
    orderNum = browser.find_element_by_name('orderNum')
    orderNum.send_keys('1')
    # 支付方式

    # 支付状态

    # 订单状态

    # 是否自营订单

    # 完成进度
    proGress = browser.find_element_by_name('progress')
    proGress.send_keys('100%')
    # 完成时间

    # 备注
    remark = browser.find_element_by_name('remark')
    remark.send_keys('总部代下单。')
    # 跟单人


def left_url(url):
    order_url = urljoin('http://crm.easyrong.com',url)
    return order_url

def main():
    url='http://crm.easyrong.com/'
    browser=webdriver.Chrome()
    browser.get(url)
    username=browser.find_element_by_id('username')
    username.send_keys('13661892653')
    password=browser.find_element_by_id('password')
    password.send_keys('xlh123456789')
    button=browser.find_element_by_class_name('btn-success')
    button.click()

    href=browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[7]/a").get_attribute('href')
    print('href',href)
    order_url=left_url(href)
    browser.get(order_url)
    #新增订单按钮
    href = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[1]/div[2]/a').get_attribute('href')
    print('href', href)
    order_url = left_url(href)
    browser.get(order_url)
    insert_content(browser,'福建东起海浪发电投资有限公司')

if __name__=="__main__":
    main()