# -*- coding: utf-8 -*-
from __future__ import absolute_import

from enum import IntEnum


class RoomType(IntEnum):
    one_one = 1
    one_n = 2
    small_course_flash = 4
    small_course_app = 8


class UserRole(IntEnum):
    teacher = 1 # 值为1时表示以 主讲人身份进入教室
    audience = 2 # 值为2时表示以听众身份进入教室
    invisible_user = 3 # 值为3时表示以隐身监课者身份进入
    assistant = 4 # 值为4时表示以房间助教身份进入教室


class DeviceType(IntEnum):
    pc = 1
    mobile = 2
