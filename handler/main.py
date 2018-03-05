from flask import Flask, Blueprint

# flaskapp的基础配置
app = Flask(__name__)
# app.config["SERVER_NAME"] = "tauw.cc"
app.config.from_object('config.flask_config')
app.jinja_env.variable_start_string = "{{ "
app.jinja_env.variable_end_string = " }}"
bp = Blueprint('flask', __name__, subdomain='flask')
app.register_blueprint(bp)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'