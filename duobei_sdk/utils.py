# -*- coding: utf-8 -*-
from __future__ import absolute_import

import hashlib


class Sign(object):

    def __init__(self, api_key):
        self.api_key = api_key

    def encode(self, params):
        data = []
        for key, val in params.iteritems():
            if val == '':
                continue
            data.append('{}={}'.format(key, val))
        data = sorted(data)
        return '{}{}'.format('&'.join(data), self.api_key)

    def sign(self, params):
        encode_string = self.encode(params)
        return hashlib.md5(encode_string).hexdigest()
