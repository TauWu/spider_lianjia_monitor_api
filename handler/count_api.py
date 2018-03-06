# -*- coding: utf-8 -*-
#
# 爬虫统计Api接口模块
#

from .main import app, web_logger
from flask import request
from util.common.date import Time
from util.common.api import api
from module.database.count_db import CountDB

@app.route(rule="/count_spider_create", methods=['GET'])
@api
def count_spider_create():
    '''
    CountSpiderCreate
    - 返回某一天的房源爬虫数量
    - 当前数据表lianjia_house_info*的数据条数
    '''
    date = request.args.get("date")

    if date is None:
        date = Time.now_date_str()
    else:
        date = date.replace("-","").replace("_","")

    countdb = CountDB()
    code, msg, count = countdb.count_house_info(date)

    return dict(date=date), code, msg, dict(date=date, count=count)

@app.route(rule="/count_spider_page", methods=['GET'])
@api
def count_spider_page():
    '''
    CountSpiderPage
    - 返回某一天的房源爬虫第二步完成的数量
    - 当前数据表lianjia_house_info*中没有house_type_new的数据条数
    '''
    date = request.args.get("date")

    if date is None:
        date = Time.now_date_str()
    else:
        date = date.replace("-","").replace("_","")

    countdb = CountDB()
    code, msg, count = countdb.count_house_info(date, "where house_type_new != \"\"")

    return dict(date=date), code, msg, dict(date=date, count=count)

@app.route(rule="/count_spider_stat", methods=['GET'])
@api
def count_spider_stat():
    '''
    CountSpoderStat
    - 返回某一天的房源第三步爬虫数量
    - 当前数据表lianjia_house_stat_json*的数据条数
    '''
    date = request.args.get("date")

    if date is None:
        date = Time.now_date_str()
    else:
        date = date.replace("-","").replace("_","")

    countdb = CountDB()
    code, msg, count = countdb.count_house_stat(date)

    return dict(date=date), code, msg, dict(date=date, count=count)

