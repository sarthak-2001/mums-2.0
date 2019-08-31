from flask import Flask, request, jsonify
from hibi_functions import login
from hibi_functions import notice
from hibi_functions import notice_content
from hibi_functions import fees

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "welcome to hibi api"


@app.route('/login_test', methods=['POST'])
def log_in():
    try:
        uid = request.json['uid']
        pwd = request.json['pwd']
        data = login.login(uid, pwd)
        # print(data)
        if data == 'fail':
            d = {'result': 'failed'}
        else:
            d = {'result': 'success'}
        return jsonify(d)

    except:
        return jsonify({'result': 'failed'})


@app.route('/notice', methods=['POST'])
def notice_d():
    try:
        uid = request.json['uid']
        pwd = request.json['pwd']
        # data = notice.notice_details(uid, pwd)
        data = notice.notice_data(uid, pwd)
        # print(data)
        # if data == 'fail':
        #     d = {'return': 'failed'}
        # else:
        #     d = {'Notices': data}
        d = {'Notices': data}

        return jsonify(d)

    except:
        return jsonify({'Notices': []})


@app.route('/notice_data', methods=['POST'])
def notice_c():
    try:
        uid = request.json['uid']
        pwd = request.json['pwd']
        id_num = request.json['id']
        # data = notice.notice_details(uid, pwd)
        data = notice_content.notice_content(uid, pwd, id_num)
        # print(data)
        d = {'Notices': data}

        return jsonify(d)

    except:
        return jsonify({'Notices': [{"notice_data":None}]})


@app.route('/fee', methods=['POST'])
def feess():

    try:
        uid = request.json['uid']
        pwd = request.json['pwd']
        data = fees.fees_extractor(uid, pwd)

        d = {'Notices': data}

        return jsonify(d)

    except:
        return jsonify({'Notices': [{"html":""}]})


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,threaded=True,debug=True)
