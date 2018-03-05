from flask import Flask, Blueprint
from util.common.logger import use_logger

@use_logger(level="info")
def web_info(msg):
    pass

@use_logger(level="warn")
def web_warn(msg):
    pass

@use_logger(level="err")
def web_err(msg):
    pass

@use_logger(level="fatal")
def web_fatal(msg):
    pass


def web_logger(level, funcname, inpara="", out=""):
    msg = "{funcname}\tIn:{inpara}\tReturn:{out}".format(funcname=\
    funcname, inpara=inpara, out=out)

    if level == "info":
        web_info(msg)
    elif level == "warn":
        web_warn(msg)
    elif level == "err":
        web_err(msg)
    elif level == "fatal":
        web_fatal(msg)

# flaskapp的基础配置
app = Flask(__name__)
# app.config["SERVER_NAME"] = "tauw.cc"
app.config.from_object('config.flask_config')
app.jinja_env.variable_start_string = "{{ "
app.jinja_env.variable_end_string = " }}"
bp = Blueprint('flask', __name__, subdomain='flask')
app.register_blueprint(bp)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
web_logger("info",__name__)