from bs4 import BeautifulSoup
import requests
import re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/24.0'}

# t=k.select('div[class="hotnews"]')
# S = re.compile('href="(.*?)"',re.S)
# res = re.findall(pattern,str(html))

def get_index():
    url = 'http://news.baidu.com/'
    response = requests.get(url,headers=headers)
    if response.status_code==200:
        soup = BeautifulSoup(response.text, 'lxml')
        hotNews=soup.select('.hotnews ul a')
        for item in hotNews:
            data={}
            data['title']=item.get_text()
            data['url'] =item.attrs['href']
            print(data)
def main():
    get_index()
if __name__=="__main__":
    main()