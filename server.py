import time
from flask import Flask, request, jsonify

from pikpak_captcha import slider_validation
app = Flask(__name__)


@app.route('/api/login', methods=['GET'])
def get_data():
    # 获取请求中的 JSON 数据
    url = request.args.get("url")
    for count in range(3):
        try:
            token = slider_validation(url) #这里就是验证模块 用于获取url的token
            break
        except:
            token = None
            time.sleep(5)
    if token and token != "":
        response_data = {
            'url_received': url,
            'token': token,
            "code": 200,
        }
        return jsonify(response_data)
    else:
        response_data = {
            'url_received': url,
            "code": -1,
        }
        return jsonify(response_data), 400


if __name__ == '__main__':
    app.run(debug=True, port=5243)
