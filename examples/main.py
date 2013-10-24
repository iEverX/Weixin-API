# -*- coding: utf-8 -*-

from flask import *
from weixin import Weixin
from replier import Replier
from ext import WSGICopyBody

import logging

app = Flask(__name__)
app.wsgi_app = WSGICopyBody(app.wsgi_app)
app.config.from_object('config')

TOKEN = app.config['TOKEN']
replier = Replier()

wx = Weixin(TOKEN, replier)

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        return wx.handle(request.environ['body_copy'])
    else:
        return wx.check_signature(request.args)


app.debug = True
app.run(host='localhost', port=9009)
