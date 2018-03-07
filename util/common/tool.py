# -*- utf-8 -*-
# 基础工具

from .date import Time

def db_exec_sql(date, sql_template, wherestr=""):
    exec_sql = str()
    if wherestr != "":
        if date == Time.now_date_str():
            exec_sql = sql_template%("", wherestr)
        else:
            exec_sql = sql_template%('_'+date, wherestr)
    else:
        if date == Time.now_date_str():
            exec_sql = sql_template%("")
        else:
            exec_sql = sql_template%('_'+date)
            
    return exec_sql

def api_date(date):
    if date is None:
        date = Time.now_date_str()
    else:
        date = date.replace("-","").replace("_","")
    return date

def pagination(request):
    page = request.args.get("page")
    pagesize = request.args.get("pagesize")

    if page is not None and pagesize is not None:
        pass
    else:
        if pagesize is None:
            pagesize = "20"
        if page is None:
            page = "1"
    return int(page), int(pagesize)

def limit_str(page, pagesize):
    start = page * pagesize
    if start < 0:
        start = 0
    return " limit %d, %d "%(start, pagesize)