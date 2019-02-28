# -*- coding: utf-8 -*-
import arrow
import time

from __secret import PARTNER_ID, APIKEY

from duobei_sdk import constants
from duobei_sdk.live import LiveAPI


def room_create():
    live_api = LiveAPI(PARTNER_ID, APIKEY)

    title = 'sdk 测试创建room v3'
    starttime = arrow.now().shift(minutes=1)
    duration = 1
    video=0
    room_type=2
    response = live_api.room_create(
        title, starttime, duration, video=video, room_type=room_type
    )
    return response


def room_create_v4():
    live_api = LiveAPI(PARTNER_ID, APIKEY)
    title = 'sdk 测试创建room v4'
    starttime = arrow.now().shift(minutes=10)
    length = 35
    video=0
    room_type=2
    response = live_api.room_create_v4(
        title, starttime, length, video=video, room_type=room_type
    )
    return response


def room_update_title(roomid, title='sdk 修改房间名字'):
    live_api = LiveAPI(PARTNER_ID, APIKEY)
    response = live_api.room_update_title(roomid, title)
    return response


def room_update_time(roomid):
    live_api = LiveAPI(PARTNER_ID, APIKEY)
    starttime = arrow.now().shift(minutes=5)
    duration = 1
    response = live_api.room_update_time(roomid, starttime, duration)
    return response


def room_update_time_v4(roomid):
    live_api = LiveAPI(PARTNER_ID, APIKEY)
    starttime = arrow.now().shift(minutes=5)
    length = 50
    response = live_api.room_update_time_v4(roomid, starttime, length)
    return response


def room_detail(roomid):
    live_api = LiveAPI(PARTNER_ID, APIKEY)
    response = live_api.room_detail(roomid)
    return response


def room_enter(roomid, role, device_type=constants.DeviceType.pc.value):
    mapper = {
        'teacher': {
            'uid': 'aaaa1',
            'nickname': 'teacher',
            'user_role': constants.UserRole.teacher.value,
        },
        'audience': {
            'uid': 'aaaa2',
            'nickname': 'audience',
            'user_role': constants.UserRole.audience.value,
        },
        'invisible_user': {
            'uid': 'aaaa3',
            'nickname': 'invisible_user',
            'user_role': constants.UserRole.invisible_user.value,
        },
        'assistant': {
            'uid': 'aaaa4',
            'nickname': 'assistant',
            'user_role': constants.UserRole.assistant.value,
        },
    }
    data = mapper[role]
    uid = data['uid']
    nickname = data['nickname']
    user_role = data['user_role']
    live_api = LiveAPI(PARTNER_ID, APIKEY)
    response = live_api.room_enter(roomid, uid, nickname, user_role, device_type)
    return response
