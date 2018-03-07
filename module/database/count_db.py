# -*- coding: utf-8 -*-

from ..database import *
from util.common.api import req_result

class CountDB(DB):

    def __init__(self):
        DB.__init__(self)

    @req_result
    def count_house_info(self, date=Time.now_date_str(), wherestr=""):
        from .sql_template import count_house_info_sql

        exec_sql = str()

        if date == Time.now_date_str():
            exec_sql = count_house_info_sql%("", wherestr)
        else:
            exec_sql = count_house_info_sql%('_'+date, wherestr)

        try:
            DB.execute(self, exec_sql)
        except Exception as e:
            return e, 0

        return None, self.cur.fetchone()[0]
    
    @req_result
    def count_house_stat(self, date=Time.now_date_str()):
        from .sql_template import count_house_stat_sql

        exec_sql = str()

        if date == Time.now_date_str():
            exec_sql = count_house_stat_sql%""
        else:
            exec_sql = count_house_stat_sql%('_'+date)

        try:
            DB.execute(self, exec_sql)
        except Exception as e:
            return e, 0

        return None, self.cur.fetchone()[0]