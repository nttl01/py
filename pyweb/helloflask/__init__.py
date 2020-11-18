from flask import Flask, g, render_template

app = Flask(__name__)
app.debug = True
app.jinja_env.trim_blocks = True

@app.route("/tmpl")
def t():
    return render_template('index.html')
      
# app.config['SEVER_NAME'] = 'local.com:5000'

# @app.route("/sd")
# def helloworld_local():
#     return "hello local.com"

# @app.route("/sd", subdomain='g')
# def helloworl_g():
#     return "hello g.local.com"


# @app.before_request
# def before_request():
#     print("before_request!!!")
#     g.str = "한글"

@app.route("/")
def helloworld():
    return "hello flask world!" + getattr(g, 'str', '111')