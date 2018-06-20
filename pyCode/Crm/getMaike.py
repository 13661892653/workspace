#coding=utf-8
#author:colby

import requests
from bs4 import BeautifulSoup

start_url='http://mikecrm.com/form.php#/submit?id=1706628'
url='http://mikecrm.com/handler/web/form_submit/handleGetListFormSubmitSummary.php'
request_headers={
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'_ga=GA1.2.650401320.1506760585; _gid=GA1.2.186151230.1529371753; PHPSESSID=a3qj5lk5h0mo08jfmolg7p6au4; uvi=3QHegvbWHI5bPjtfk2i1ajnxo3BfrM8uANJOiUKYBN9q7C01; _gat=1',
    'Host': 'mikecrm.com',
    'Origin': 'http://mikecrm.com',
    'Referer': 'http://mikecrm.com/form.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

def login_maike():
    resonse=requests.get(url,headers=request_headers)
    soup=BeautifulSoup(resonse.text,'lxml')
    print(soup)


def get_one_page_enterprise():
    pass

def parse_one_page_enterprise():
    pass

def get_many_page_enterprise():
    pass

def main():
    login_maike()


if __name__ == "__main__":
    main()

