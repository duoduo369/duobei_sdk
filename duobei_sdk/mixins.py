# -*- coding: utf-8 -*-
import arrow
import copy
import logging
import time
import requests

from . import exceptions
from .utils import Sign


class APIMixin(object):

    def __init__(self, partner_id, api_key):
        self.partner_id = partner_id
        self.api_key = api_key
        self.sign = Sign(api_key)

    def get_api_prefix(self):
        raise NotImplementedError()

    def get_url(self, path):
        api_prefix = self.get_api_prefix()
        return '{}{}'.format(api_prefix, path)

    def request(self, url, params, method='get', timeout=3, response_format_type='json'):
        if not isinstance(params, dict):
            raise exceptions.DuobeiSDKInvalidParamException()
        sign = self.sign.sign(params)
        _params = copy.deepcopy(params)
        _params['sign'] = sign
        if method == 'get':
            response = requests.get(url, params=_params, timeout=timeout)
        elif method == 'post':
            response = requests.post(url, data=_params, timeout=timeout)
        else:
            raise NotImplementedError()
        if response_format_type == 'json':
            data = response.json()
            if not data['success']:
                logging.error('[DuobeiSDK request error]: %s', data)
                raise exceptions.DuobeiSDKServerException(str(data))
        else:
            data = response.content
        return data

    def get_now_timestamp(self):
        timestamp = int(time.time() * 1000)
        return timestamp

    def tzone_to_shanghai(self, _datetime):
        return arrow.get(_datetime).to('Asia/Shanghai')
