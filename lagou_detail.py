# -*-coding:utf-8-*-
# -*- author:wolfog-*-
# purpose:从数据库中拿出职位的id，然后请求具体数据根据Beautiful拿到具体的职位要求

import requests
from bs4 import BeautifulSoup
import pymongo
import time


def getDetail(positionID, postfix):
    url = 'https://www.lagou.com/jobs/{}.html'.format(positionID)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'cache-control': 'max-age=0',
        'Cookie': 'user_trace_token=20171216104212-b7dfc4ef-e20a-11e7-9be6-525400f775ce; LGUID=20171216104212-b7dfc7d6-e20a-11e7-9be6-525400f775ce; index_location_city=%E6%B7%B1%E5%9C%B3; isCloseNotice=0; JSESSIONID=ABAAABAACBHABBI45673CE7D446AB49A9A9F353EC8B17ED; X_HTTP_TOKEN=d4520d7e09a442d140b922e9a0f82aea; TG-TRACK-CODE=search_code; SEARCH_ID=7814c370bd0449cd8e31e01d38ca5c79; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F2983824.html; _gid=GA1.2.1200137293.1514363686; _ga=GA1.2.1520875858.1514363686; LGSID=20171227174809-0b8b96db-eaeb-11e7-b147-525400f775ce; LGRID=20171227181042-3208c353-eaee-11e7-b147-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1514363687,1514363695,1514363707; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1514369445',
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98?city=%E6%B7%B1%E5%9C%B3&cl=false&fromSearch=true&labelWords=&suginput=',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    }
    print(url)
    resq = requests.get(url, headers=headers)
    soup = BeautifulSoup(resq.text, 'lxml')
    des_parent_tab = soup.select('#job_detail > dd.job_bt > div >  p')
    detailContent = []
    for item in des_parent_tab:
        print(item.text)
        detailContent.append(item.text)
    client['lagouDb']['data_sz_colls{}'.format(postfix)].update({'positionId': positionID},
                                                                {'$set': {"requirement": detailContent}})
    print("=" * 90 + "end" + "=" * 90)


client = pymongo.MongoClient('localhost', 27017)
# result = client.lagouDb.data_sz_colls数据分析.find().limit(3)推荐使用下面的写法，比较灵活
# postfixList = ['数据分析', '数据挖掘', '数据分析实习', '数据实习', '数据运营', '数据分析助理', '数据挖掘实习','数据实习']
postfixList = ['深度学习', '算法', '自然语言处理', '机器学习实习', '计算机视觉', '人工智能', '大数据']
# 到数据实习了
for postfix in postfixList:
    print("=" * 90 + postfix + "=" * 90)
    result = client['lagouDb']['data_sz_colls{}'.format(postfix)].find()
    for item in result:
        print(item['positionId'])
        time.sleep(2)
        getDetail(item['positionId'], postfix)
