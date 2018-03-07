# -*- coding: utf-8 -*-

import json
from .logger import base_info

def api(func):
    '''生成Api装饰器
    要求函数返回参数：
    - 传入参数、返回码、返回信息、数据
    - 传入参数、返回码、返回信息、数据、页码信息
    '''  
    def wrapper(*args, **kwargs):
        func_rtn = func(*args, **kwargs)
        ins = func_rtn[0]
        code = func_rtn[1]
        msg = func_rtn[2]
        data = func_rtn[3]

        base_info("Handler:%s Code:%d Msg:%s In:%s Return:%s"%(func.__name__, code, msg, ins, data))
        
        if len(func_rtn) == 4:
            return json.dumps(dict(data=data, code=code, message=msg))
        if len(func_rtn) == 5:
            pagination = func_rtn[4]
            return json.dumps(dict(data=data, code=code, message=msg, pagination=pagination))
    
    wrapper.__name__ = func.__name__
    return wrapper

def req_result(func):
    '''数据库操作Api返回
    要求函数返回参数：
    - 错误内容、返回数据
    - 错误内容、返回数据、总数量
    '''
    def wrapper(*args, **kwargs):
        func_rtn = func(*args, **kwargs)
        err = func_rtn[0]
        rtn = func_rtn[1]
        if err is not None:
            code, msg = 1, str(err)
        else:
            code, msg = 0, 'success.'
        if len(func_rtn) == 3:
            return code, msg, rtn, func_rtn[2]
        return code, msg, rtn
    wrapper.__name__ = func.__name__
    return wrapper
