# Weixin API

A very simple weixin api.

## Usage

    # initial like this
    # :param token: the token you set at weixin platform
    # :param replier: see the replier section
    wx = Weixin(token, replier)

    # check signature like this
    # :param p: a dict contains the weixin api parameters
    wx.check_signature(p)

    # handle a request like this
    # this function return a unicode string
    # :param data: the xml passed in by weixin server
    wx.handle(data)

## Replier

A replier is a class that implements following methods to response to the corresponding request.

* `reply_to_text`
* `reply_to_image`
* `reply_to_location`
* `reply_to_link`
* `reply_to_event`

If any of methods is not implemented, there should be a `reply` method in case that you make sure the corresponding request will never come.

When a request comes, the corresponding method if exists otherwise the method `reply` will handle it. It will raise exception if no one exists.

All the `reply*` methods takes one dict parameter that contains the data of xml passed from weixin server.