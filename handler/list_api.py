# -*- coding: utf-8 -*-
#
# 爬虫获取的房源列表Api接口模块
#

from .main import app, web_logger
from flask import request
from util.common.date import Time
from util.common.api import api
from util.common.tool import api_date, pagination, limit_str
from module.database.list_db import ListDB

@app.route(rule="/list_house_id", methods=['GET'])
@api
def list_house_id():
    '''
    ListHouseID
    - 返回经过筛选条件筛选的ID列表（限定pagesize）
    '''

    date = api_date(request.args.get("date"))
    page, pagesize = pagination(request)
    distinct = request.args.get("district")

    where_str = "where 1 = 1 %s"
    limit = limit_str(page, pagesize)

    if distinct is not None:
        where_str = where_str%(" and district = \"%s\" "%distinct)
    else:
        where_str = where_str%""

    list_db = ListDB()
    code, msg, rtn, total = list_db.list_house_id(date, where_str, limit)

    return dict(date=date, page=page, pagesize=pagesize, distinct=distinct), code, msg, dict(house_id_list=rtn), dict(page=page, pagesize=pagesize, total=total)