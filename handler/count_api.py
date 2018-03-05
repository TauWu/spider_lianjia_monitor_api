# -*- coding: utf-8 -*-
#
# 爬虫统计Api接口模块
#

from .main import app, web_logger
from flask import request
from util.common.date import Time

@app.route(rule="/count_house_insert", methods=['GET'])
def count_house_insert():
    '''
    CountHouseInsert
    - 返回某一天的房源爬虫数量
    - 当前数据表lianjia_house_info*的数据条数
    '''
    from module.database.count_db import CountDB

    date = request.args.get("date")

    if date is None:
        date = Time.now_date_str()

    countdb = CountDB()
    try:
        count = countdb.count_house_info(date)
    except countdb.IntegrityError:
        pass

    return """{"date":%s,"count":%d}"""%(date,count)

