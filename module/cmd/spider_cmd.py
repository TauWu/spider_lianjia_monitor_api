# -*- coding: utf-8 -*-

from ..cmd import *
from .cmd_template import ps_cmd_str
from pprint import pprint
from util.common.api import req_result

@req_result
def spider_cmd(process_name):
    try:
        a = Popen(ps_cmd_str%(process_name), stdout=PIPE, shell=True)
        stdouts = a.stdout.readlines()
        stdouts = [dict(zip(['pid','stime','time','cmd'], list(str(stdout)[2:-3].split(' ')))) for stdout in stdouts]
    except Exception as e:
        return str(e), None
    return None, stdouts