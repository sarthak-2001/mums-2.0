from flask import Flask, request, jsonify
from hibi_functions import login
from hibi_functions import notice

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "welcome to hibi api"


# @app.route('/test')
# def test():
#     x = request.json['x']
#     y = request.json['y']
#     c = testtt.np(x,y)
#     print(c)
#     return "calll"

@app.route('/api/login')
def log_in():
    uid = request.json['uid']
    pwd = request.json['pwd']
    data =  login.login(uid, pwd)
    # print(data)
    if data == 'fail':
        d = {'return': 'failed'}
    else:
        d = {'return': 'success'}
    return jsonify(d)


@app.route('/api/notices')
def notice_d():
    uid = request.json['uid']
    pwd = request.json['pwd']
    # data = notice.notice_details(uid, pwd)
    data = notice.notice_data(uid, pwd)
    # print(data)
    if data == 'fail':
        d = {'return': 'failed'}
    else:
        d = {'Notices': data}

    return jsonify(d)


if __name__ == "__main__":
    app.run(debug=True)
