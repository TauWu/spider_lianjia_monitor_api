# -*- coding: utf-8 -*-
#
# 爬虫获取的房源详情信息Api接口模块
#

from .main import app, web_logger
from flask import request
from util.common.date import Time
from util.common.api import api
from module.database.count_db import CountDB