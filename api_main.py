# -*- coding: utf-8 -*-

# 模块引用
from flask import Flask, request, render_template, jsonify, g, Blueprint, session, redirect, url_for
import requests
import json

# flaskapp的基础配置
app = Flask(__name__)
# app.config["SERVER_NAME"] = "tauw.cc"
app.config.from_object('config.flask_config')
app.jinja_env.variable_start_string = "{{ "
app.jinja_env.variable_end_string = " }}"
bp = Blueprint('flask', __name__, subdomain='flask')
app.register_blueprint(bp)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/test", methods=['GET'])
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

    if req_content["code"] == 0:
        success = True
        message = "日期：{date}\n日出时间：{time_rise}\n日落时间：{time_down}".format(date=date, \
        time_rise=req_content["data"]["sun_rise_time"],time_down=req_content["data"]["sun_down_time"])
    else:
        success = False
        message = req_content["message"]
    
    return render_template('test.html', success=success, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
