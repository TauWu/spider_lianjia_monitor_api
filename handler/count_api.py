# -*- coding: utf-8 -*-
#
# 爬虫统计Api接口模块
#

from .main import app, web_logger
from flask import request
from util.common.date import Time
from util.common.api import api
from module.database.count_db import CountDB

@app.route(rule="/count_house_insert", methods=['GET'])
@api
def count_house_insert():
    '''
    CountHouseInsert
    - 返回某一天的房源爬虫数量
    - 当前数据表lianjia_house_info*的数据条数
    '''
    date = request.args.get("date").replace("-","").replace("_","")

    if date is None:
        date = Time.now_date_str()

    countdb = CountDB()
    code, msg, count = countdb.count_house_info(date)

    return dict(date=date), code, msg, dict(date=date, count=count)

@app.route(rule="/count_stat_insert", methods=['GET'])
@api
def count_stat_insert():
    '''
    CountStatInsert
    - 返回某一天的房源第三步爬虫数量
    - 当前数据表lianjia_house_stat_json*的数据条数
    '''
    date = request.args.get("date").replace("-","").replace("_","")

    if date is None:
        date = Time.now_date_str()

    countdb = CountDB()
    code, msg, count = countdb.count_house_stat(date)

    return dict(date=date), code, msg, dict(date=date, count=count)

