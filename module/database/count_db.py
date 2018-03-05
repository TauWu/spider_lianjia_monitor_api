# -*- coding: utf-8 -*-

from ..database import *

class CountDB(DB):

    def __init__(self):
        DB.__init__(self)
        self.today = Time.now_date_str

    def count_house_info(self, date=Time.now_date_str()):
        from .sql_template import count_house_info_sql

        exec_sql = str()

        if date == Time.now_date_str():
            exec_sql = count_house_info_sql%""
        else:
            exec_sql = count_house_info_sql%('_'+date)
        
        DB.execute(self, exec_sql)
        return self.cur.fetchone()[0]