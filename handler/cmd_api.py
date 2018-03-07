# -*- coding: utf-8 -*-

from .main import app, web_logger
from flask import request
from util.common.date import Time
from util.common.api import api
from module.cmd.spider_cmd import spider_cmd

@app.route(rule="/cmd_spider", methods=['GET'])
@api
def cmd_spider():
    '''
    CMDSpider
    - 返回某一程序是否正在进行以及对应进程的相关信息
    '''

    proc_name = request.args.get("proc_name")

    if proc_name is None:
        proc_name = "spider"

    code, msg, rtn = spider_cmd(proc_name)

    return dict(proc_name=proc_name), code, msg, rtn
    