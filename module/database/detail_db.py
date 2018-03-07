# -*- coding: utf-8 -*-

from ..database import *
from util.common.api import req_result

class DetailDB(DB):

    def __init__(self):
        DB.__init__(self)

    @req_result
    def detail_house_info(self, house_id, date=Time.now_date_str()):
        from .sql_template import detail_house_info_sql
        from .sql_rtn_list import detail_house_info_rtn_list

        exec_sql = str()

        if date == Time.now_date_str():
            exec_sql = detail_house_info_sql.format(date="", house_id=house_id)
        else:
            exec_sql = detail_house_info_sql.format(date='_'+date, house_id=house_id)

        try:
            DB.execute(self, exec_sql)
        except Exception as e:
            return e, None

        db_rtn = self.cur.fetchone()

        if db_rtn == None:
            return None, None

        rtn = dict(zip(detail_house_info_rtn_list, db_rtn))

        return None, rtn

    @req_result
    def detail_house_stat(self, house_id, date=Time.now_date_str()):
        from .sql_template import detail_house_stat_sql
        from .sql_rtn_list import detail_house_stat_rtn_list
        import json

        exec_sql = str()

        if date == Time.now_date_str():
            exec_sql = detail_house_stat_sql.format(date="", house_id=house_id)
        else:
            exec_sql = detail_house_stat_sql.format(date='_'+date, house_id=house_id)

        try:
            DB.execute(self, exec_sql)
        except Exception as e:
            return e, None

        db_rtn = self.cur.fetchone()
        db_rtn = list(db_rtn)

        if db_rtn == None:
            return None, None

        json_rtn = json.loads(str(db_rtn[2]))
        db_rtn[2] = json_rtn
        rtn = dict(zip(detail_house_stat_rtn_list, db_rtn))

        return None, rtn
