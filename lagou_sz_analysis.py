# -*-coding:utf-8-*-
# -*- author:wolfog-*-
# purpose：分析拉钩上跟数据挖掘，数据分析等相近的岗位要求，全国的
# 1、使用request 直接获得json数据
# 2、或者使用Beautiful来拿到数据。

import json

import requests
import pymongo

keyword = ['数据分析', '数据挖掘', '数据分析实习', '数据实习', '数据运营', '数据分析助理', '数据挖掘实习']


def getCountryData(i, j):
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false&isSchoolJob=0&city=深圳'
    # 关于data的说明，first表示的是否首页，pn表示页数。
    data = {
        'first': False if i == 1 else True,
        'pn': str(i),
        'kd': keyword[j]
    }
    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '55',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'user_trace_token=20171216104212-b7dfc4ef-e20a-11e7-9be6-525400f775ce; LGUID=20171216104212-b7dfc7d6-e20a-11e7-9be6-525400f775ce; index_location_city=%E6%B7%B1%E5%9C%B3; TG-TRACK-CODE=search_code; JSESSIONID=ABAAABAABEEAAJA8BEA8C22CA04C3109B8F977DA7E7A2D1; _gat=1; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%3Foquery%3D%25E6%2595%25B0%25E6%258D%25AE%26fromSearch%3Dtrue%26labelWords%3Drelative; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%3Fpx%3Ddefault%26city%3D%25E5%2585%25A8%25E5%259B%25BD; _gid=GA1.2.586433213.1513392135; _ga=GA1.2.129524208.1513392135; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1513392136; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1513403412; LGSID=20171216134920-dc6d5db8-e224-11e7-9bf0-525400f775ce; LGRID=20171216135008-f916cdd3-e224-11e7-9bf0-525400f775ce; SEARCH_ID=126ef42874c34a99bc99f9ad06076942',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?px=default&city=%E5%85%A8%E5%9B%BD',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'X-Anit-Forge-Code': '0',
        'X-Requested-With': 'XMLHttpRequest',
    }
    resq = requests.post(url, headers=header, data=data)
    json_dict = json.loads(resq.content)
    lists = json_dict['content']['positionResult']['result']
    for list in lists:
        data = {
            'city': list['city'],
            'companyFullName': list['companyFullName'],
            'companySize': list['companySize'],
            'financeStage': list['financeStage'],
            'firstType': list['firstType'],
            'secondType': list['secondType'],
            'industryField': list['industryField'],
            'positionName': list['positionName'],
            'salary': list['salary'],
            'workYear': list['workYear'],
            'district': list['district'],
            'positionId': list['positionId'],
            ' createTime': list['createTime'],
        }
        client['lagouDb']['data_sz_colls' + keyword[j]].insert_one(data)


if __name__ == '__main__':
    client = pymongo.MongoClient('localhost', 27017)
    for j in range(0, 7):
        for i in range(1, 31):  # 深圳只有336个岗位
            print("%s的第%d页" % (keyword[j], i))
            getCountryData(i, j)
