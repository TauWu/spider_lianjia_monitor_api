# -*- coding: utf-8 -*-
#
# 爬虫获取的房源详情信息Api接口模块
#

from .main import app, web_logger
from flask import request
from util.common.date import Time
from util.common.api import api
from util.common.tool import api_date
from module.database.detail_db import DetailDB

@app.route(rule="/detail_house_info", methods=['GET'])
@api
def detail_house_info():
    '''
    DetailHouseInfo
    - 返回某一天 某一个房源编号的 详情信息
    '''

    date = api_date(request.args.get("date"))
    house_id = request.args.get("house_id")

    detail_db = DetailDB()
    code, msg, rtn = detail_db.detail_house_info(house_id, date)

    return dict(date=date, house_id=house_id), code, msg, rtn

@app.route(rule="/detail_house_stat", methods=['GET'])
@api
def detail_house_stat():
    '''
    DetailHouseStat
    - 返回某一天 某一个房源编号的 统计信息
    '''

    date = api_date(request.args.get("date"))
    house_id = request.args.get("house_id")

    detail_db = DetailDB()
    code, msg, rtn = detail_db.detail_house_stat(house_id, date)

    return dict(date=date, house_id=house_id), code, msg, rtn
