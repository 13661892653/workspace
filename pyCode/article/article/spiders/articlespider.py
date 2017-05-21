# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider
from scrapy import Request
from urllib import parse

class JobboleSpider(CrawlSpider):
    name = "jobbole"
    redis_key = "JobboleSpider:start_urls"
    #allowed_domains = ["http://blog.jobbole.com/"]
    start_urls = ['http://blog.jobbole.com/all-posts/']
    def parse_details(self, response):
        print("asdfasdfasdfsajfdlkasjdflkasjdfljas;ldfjasl")
        # 提取而文章详情页信息逻辑
        print("sdjflskdjflsakjdflasjdflkasjdflkjasdlf")
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        create_time = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace("·",
                                                                                                                    "")
        favor_count = int(response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0])
        collect_count = response.css(".bookmark-btn::text").extract()[0]
        collect_match = re.match(".*?(\d+).*", collect_count)
        if collect_match:
            collect_count = int(collect_match.group(1))
        else:
            collect_count = 0

        tag_list = response.css(".entry-meta-hide-on-mobile a::text").extract()
        for tag in tag_list:
            print(tag)
    def parse(self, response):
        alltitle_urls = response.css("#archive .floated-thumb .post-thumb a::attr(href)").extract()
        print('response.url',response.url)
        for title_url in alltitle_urls:
            #print(parse.urljoin(response.url, title_url))
            yield Request(parse.urljoin(response.url, title_url),callback=self.parse_details)
        # next_url = response.css(".next.page-numbers::attr(href)").extract_first()
        # if next_url:
        #     yield Request(url=urlparse.urljoin(response.url, title_url), callback=self.parse)


