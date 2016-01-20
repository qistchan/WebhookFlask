#-*- coding:utf-8 -*-
from flask import Flask
from flask import request
from WebHook_Function import *

app = Flask(__name__)

@app.route('/deploy', methods=['POST','GET'])
def checkPostData():
    if request.method == 'GET':
        return 'Empty!', 404
    if request.method == 'POST':
        if not request.form:
            return 'Invalid Data', 400
        if not check(request.headers.get('User-Agent')):
            return 'Invalid Data!', 400
        else:
            return deploy()

if __name__ == '__main__':
    app.run(host=read_config()['Host'], port=read_config()['Port'])
