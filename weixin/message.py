# -*- coding: utf-8 -*-

TPL_TEXT = u'''<xml>
<ToUserName><![CDATA[%%s]]></ToUserName>
<FromUserName><![CDATA[%%s]]></FromUserName>
<CreateTime><![CDATA[%%s]]></CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%(content)s]]></Content>
<FuncFlag>%(flag)s</FuncFlag>
</xml>'''

TPL_MUSIC = u'''<xml>
<ToUserName><![CDATA[%%s]]></ToUserName>
<FromUserName><![CDATA[%%s]]></FromUserName>
<CreateTime>%%s</CreateTime>
<MsgType><![CDATA[music]]></MsgType>
<Music>
<Title><![CDATA[%(title)s]]></Title>
<Description><![CDATA[%(desc)s]]></Description>
<MusicUrl><![CDATA[%(music_url)s]]></MusicUrl>
<HQMusicUrl><![CDATA[%(hq_music_url)s]]></HQMusicUrl>
</Music>
<FuncFlag>%(flag)s</FuncFlag>
</xml>'''

TPL_NEWS = u'''<xml>
<ToUserName><![CDATA[%%s]]></ToUserName>
<FromUserName><![CDATA[%%s]]></FromUserName>
<CreateTime>%%s</CreateTime>
<MsgType><![CDATA[news]]></MsgType>
<ArticleCount>%s</ArticleCount>
<Articles>%s</Articles>
<FuncFlag>%(flag)s</FuncFlag>
</xml>'''

TPL_NEWS_ITEM = u'''<item>
<Title><![CDATA[%(title)s]]></Title>
<Description><![CDATA[%(description)s]]></Description>
<PicUrl><![CDATA[%(picurl)s]]></PicUrl>
<Url><![CDATA[%(url)s]]></Url>
</item>'''


class TextMessage(object):

    def __init__(self, content, flag=0):
        self._s = TPL_TEXT % locals()

    def __str__(self):
        return self._s


class MusicMessage(object):

    def __init__(self, title, description, music_url, hq_music_url, flag=0):
        self._s = TPL_MUSIC % locals()

    def __str__(self):
        return self._s


class NewsMessage(object):

    def __init__(self, count, articles, flag=0):
        seq = []
        for x in range(count):
            seq.append(TPL_NEWS_ITEM % articles[x])
        self._s = TPL_NEWS % (count, ''.join(seq))

    def __str__(self):
        return self._s
