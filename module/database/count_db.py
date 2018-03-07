# -*- coding: utf-8 -*-

from ..database import *
from util.common.api import req_result
from util.common.tool import db_exec_sql

class CountDB(DB):

    def __init__(self):
        DB.__init__(self)

    @req_result
    def count_house_info(self, date=Time.now_date_str(), wherestr=" "):
        from .sql_template import count_house_info_sql

        exec_sql = db_exec_sql(date, count_house_info_sql, wherestr)

        try:
            DB.execute(self, exec_sql)
        except Exception as e:
            return e, 0

        return None, self.cur.fetchone()[0]
    
    @req_result
    def count_house_stat(self, date=Time.now_date_str()):
        from .sql_template import count_house_stat_sql

        exec_sql = db_exec_sql(date, count_house_stat_sql)

        try:
            DB.execute(self, exec_sql)
        except Exception as e:
            return e, 0

        return None, self.cur.fetchone()[0]