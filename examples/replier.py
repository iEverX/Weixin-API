# -*- coding: utf-8 -*-

from weixin.message import TextMessage

class Replier(object):

    def reply(self, data):
        return TextMessage('some message to text')
