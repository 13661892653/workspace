# -*- coding: utf-8 -*-

# Scrapy settings for gkcx project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

BOT_NAME = 'gkcx'

SPIDER_MODULES = ['gkcx.spiders']
NEWSPIDER_MODULE = 'gkcx.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'gkcx (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'UM_distinctid=1642f4702040-091324917d5056-47e1838-1fa400-1642f470205b3f; sys_wenda_info=; areaid=51; CNZZDATA1261518471=135575566-1529801975-https%253A%252F%252Fwww.baidu.com%252F%7C1529801975; CNZZDATA1254844067=55803383-1529803479-https%253A%252F%252Fgkcx.eol.cn%252F%7C1529803479; CNZZDATA1261518421=1977681468-1529803508-%7C1529803514; CNZZDATA1254806556=1628351434-1529803535-https%253A%252F%252Fgkcx.eol.cn%252F%7C1529803535; CNZZDATA1254806670=13166609-1529803609-https%253A%252F%252Fgkcx.eol.cn%252F%7C1529803609; CNZZDATA1254806256=1846930771-1529803672-https%253A%252F%252Fgkcx.eol.cn%252F%7C1529803672; CNZZDATA1254837810=1599878878-1529803808-https%253A%252F%252Fgkcx.eol.cn%252F%7C1529803808; CNZZDATA1254844738=1987485127-1529807804-null%7C1529807804; CNZZDATA1254843501=2060140689-1529807894-https%253A%252F%252Fgkcx.eol.cn%252F%7C1529807894; CNZZDATA1000439364=1681681157-1529807834-null%7C1529808233; schoolName=??μ?-??§?????¤§?-|,????o??¤§?-|; CNZZDATA4696252=cnzz_eid%3D1463386977-1529801556-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1529822660; lastvisit=1529822643745',
    'Host': 'gkcx.eol.cn',
    'Remote Address': '211.151.94.201:443',
    'Referrer Policy': 'no-referrer-when-downgrade',
    'If-Modified-Since': 'Sat, 23 Jun 2018 15:55:23 GMT',
    'Referer': 'https://gkcx.eol.cn/soudaxue/queryProvinceScore.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.18 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'gkcx.middlewares.GkcxSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'gkcx.middlewares.GkcxDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'gkcx.pipelines.GkcxPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
