#coding=utf-8
from bs4 import BeautifulSoup
import requests

url="https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html"

webData=requests.get(url)
Soup=BeautifulSoup(webData.text,'lxml')
titles=Soup.select('div.listing_title > a')
images=Soup.select('div.photo_booking.non_generic > a > img[width="180"]')
scores=Soup.select('div.rating > span.more > a')
print(images)
for title,image,score in zip(titles,images,scores):

    data={
        'title':title.get_text(),
        'image':image.get('src'),
        'score':score.get_text(),
    }
    print(data)