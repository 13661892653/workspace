#coding=utf-8
import requests
import re
import urllib.request
import time
import json
from lxml import etree
selector=etree.HTML('ddddd')
content=selector.xpath('ul[@id="useful"]/li/text()')
#标签套标签

