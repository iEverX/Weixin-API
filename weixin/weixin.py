# -*- coding: utf-8 -*-

from hashlib import sha1
from xml.etree import ElementTree as ET
import time

TEXT = u'text'
IMAGE = u'image'
LOCATION = u'location'
LINK = u'link'
EVENT = u'event'


class Weixin(object):

    def __init__(self, token, replier):
        self.token = token
        self.replyier = replier

    def check_signature(self, params):
        signature = params.get('signature', '')
        timestamp = params.get('timestamp', '')
        nonce = params.get('nonce', '')
        echostr = params.get('echostr', '')

        args = sorted([self.token, timestamp, nonce])
        mysig = sha1(''.join(args)).hexdigest()
        return echostr if mysig == signature else '.%s' % echostr

    def handle(self, data):
        params = self._parse(data)
        msg = self._reply(params)
        return unicode(msg) % (
            params['FromUserName'],
            params['ToUserName'],
            int(time.time()))

    def _parse(self, xml):
        root = ET.fromstring(xml)
        return {unicode(node.tag): unicode(node.text) for node in root}

    def _reply(self, data):

        def _mk_func(t):
            try:
                return getattr(self.replyier, 'reply_to_%s' % t)
            except:
                return getattr(self.replyier, 'reply')

        msg_type = data.pop('MsgType', TEXT)
        return _mk_func(msg_type)(data)
