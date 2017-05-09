#!/usr/bin/python
#coding=utf-8
#DevTools:Pycharm 2017.1.2
#Env:Python 3.5
#Author:lun.chen
# -*- coding: UTF-8 -*-
import urllib
import urllib.parse
import urllib.request
import json
def youdao(word):
    qword = urllib.parse.quote(word)
    baseur1 = r'http://fanyi.youdao.com/openapi.do?keyfrom=pythontry1&key=1203296434&type=data&doctype=json&version=1.1&q='
    url = baseur1 + qword
    resp = urllib.request.urlopen(url)
    fanyi = json.loads(resp.read())

    if 'basic' in fanyi.keys():
        trans = u'%s: %s  %s\n网络释义: %s' % (
        fanyi['query'], ''.join(fanyi['translation']), ''.join(fanyi['basic']['explains']),
        ''.join(fanyi['web'][0]['value']))
        return trans
    else:
        return u'对不起，您输入的单词%s无法翻译' % word


while True:
    Neword = input('输入单词或词语：')
    if Neword == '.':
        break
    else:
        print(youdao(Neword))