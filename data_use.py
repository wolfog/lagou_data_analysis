# -*-coding:utf-8-*-
# -*- author:wolfog-*-
# purpose:使用爬取到的数据

import pymongo

client = pymongo.MongoClient('localhost', 27017)


def cityResult(parms, j):
    if j == 0:
        result = client.lagouDb.data_sz_colls数据分析.find()
    elif j == 1:
        result = client.lagouDb.data_sz_colls数据分析助理.find()
    elif j == 2:
        result = client.lagouDb.data_sz_colls数据分析实习.find()
    elif j == 3:
        result = client.lagouDb.data_sz_colls数据实习.find()
    elif j == 4:
        result = client.lagouDb.data_sz_colls数据挖掘.find()
    elif j == 5:
        result = client.lagouDb.data_sz_colls数据挖掘实习.find()
    elif j == 6:
        result = client.lagouDb.data_sz_colls数据运营.find()
    elif j == 7:
        result = client.lagouDb.data_sz_colls.find()
    a = []
    dict = {}
    for item in result:
        a.append(item[parms])
    for i in a:
        counts = a.count(i)
        if counts > 1:
            dict[i] = counts
    for key in dict:
        print(key)
    for value in dict:
        print(dict[value])
    print(str(j) * 150)


for j in range(0, 8):
    # cityResult('city',j)
    # cityResult('companySize',j)
    # cityResult('financeStage',j)
    # cityResult('firstType',j)
    # cityResult('secondType',j)
    # cityResult('industryField',j)
    # cityResult('positionName',j)
    cityResult('salary', j)
    # cityResult('workYear',j)
    # cityResult('district', j)
