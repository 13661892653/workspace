#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
import urllib.request
def nowplaying_movies(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
    req = urllib.request.Request(url, headers=headers)
    s = urllib.request.urlopen(req)
    print(s.read())
    #parser = MovieParser()
    #parser.feed(s.read())
    s.close()
    #return parser.movies

if __name__ == '__main__':
    url = 'https://movie.douban.com/cinema/nowplaying/lanzhou/'
    movies = nowplaying_movies(url)
