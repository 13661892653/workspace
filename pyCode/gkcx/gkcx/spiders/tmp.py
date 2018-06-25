# coding=utf-8
import requests
import json

if __name__ == '__main__':

    url = 'https://gkcx.eol.cn/soudaxue/queryProvinceScore.html'

    headers={
        'Accept': '*/*',
        'Host': 'data-gkcx.eol.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36',

    }
    for i in range(1, 34):
        data = {"messtype": "json",
                "page": i,
                "size": 50,
                'callback':'jQuery183027591608275984925_1529901635207',
                "_": "1529901635207",
                }
        school_datas = requests.post(url, data=data,headers=headers).text
        print(school_datas)
        # datas = school_datas["school"]
        # for data in datas:
        #     row.add_row((data["province"], data["year"], data["bath"], data["type"], data["score"]))
