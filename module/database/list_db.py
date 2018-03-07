# -*- coding:utf-8 -*-

from ..database import *
from util.common.api import req_result
from util.common.tool import db_exec_sql

class ListDB(DB):

    def __init__(self):
        DB.__init__(self)

    @req_result
    def list_house_id(self, date=Time.now_date_str(), wherestr=" ", limit=""):
        from .sql_template import list_house_id_sql
        from .sql_template import count_house_info_sql

        exec_sql = db_exec_sql(date, list_house_id_sql, wherestr+limit)
        exec_count_sql = db_exec_sql(date, count_house_info_sql, wherestr)

        print(exec_sql, exec_count_sql)

        try:
            DB.execute(self, exec_count_sql)
        except Exception as e:
            return e, None, 0
        
        total = self.cur.fetchone()[0]

        try:
            DB.execute(self, exec_sql)
        except Exception as e:
            return e, None, 0

        rtns = self.cur.fetchall()
        rtns = [rtn[0] for rtn in rtns]

        return None, rtns, total