import json, requests
from flask import request, render_template
from .main import app, web_logger

@app.route(rule="/test", methods=['GET'])
def test():
    '''
    TestPage
    - 主要为显示日出日落时间

    '''
    date = request.args.get("date")

    test_url = "http://remote.seuxw.cn/test?date={date}".format(date=date)
    req_content = json.loads(str(requests.get(test_url).text))

    success = False
    message = str()

    if date is None:
        message="请携带参数date"
        web_logger("info", __name__, """{"date":None}""", message)
        return render_template('test.html', sucess=False, message=message)

    if req_content["code"] == 0:
        success = True
        message = "日期：{date} - 日出时间：{time_rise} - 日落时间：{time_down}".format(date=date, \
        time_rise=req_content["data"]["sun_rise_time"],time_down=req_content["data"]["sun_down_time"])
    else:
        success = False
        message = req_content["message"]

    web_logger("info", __name__, """{"date":"%s"}"""%date, message)
    
    return render_template('test.html', success=success, message=message)