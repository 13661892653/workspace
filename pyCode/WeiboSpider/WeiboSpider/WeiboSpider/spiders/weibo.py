# -*- coding: utf-8 -*-
from scrapy import FormRequest
from scrapy import Spider


class WeiboSpider(Spider):
    name = "weibo"
    redis_key = "weibo:start_urls"
    start_urls = ['https://weibo.cn/search/mblog']
    allowed_domains = ['weibo.cn']
    max_page = 100

    def parse_index(self, response):
        print('dddddddddddddddddddddddddddddddd')
        weibos = response.xpath('//div[class="c" and contains(@id, "M_")]')
        print(weibos)

    def start_requests(self):
        keyword = '000001'
        url = '{url}?keyword={keyword}'.format(url=self.start_urls[0], keyword=keyword)
        for page in range(self.max_page + 1):
            data = {
                'mp': str(self.max_page),
                'page': str(page)
            }
            yield FormRequest(url, formdata=data,callback=self.parse_index )

