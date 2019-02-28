# -*- coding: utf-8 -*-
'''
直播类课程
http://docs.duobeiyun.com/
2019/02/27
'''
import arrow
from . import constants
from .mixins import APIMixin


class LiveAPI(APIMixin):

    def get_api_prefix(self):
        return 'https://api.duobeiyun.com/api/'

    def room_create(self, title, starttime, duration, video=0, room_type=2):
        '''
        创建房间
        URL
        https://api.duobeiyun.com/api/v3/room/create

        参数名  必填(Y/N)   说明
        partner Y   合作 id
        sign    Y   加密校验值
        timestamp   Y   从 1970 到现在的时间差的毫秒数, 该时间戳的有效期是 5 分钟
        title   Y   房间标题
        video   Y   是否开启视频。开启视频填1，不开启填0
        startTime   Y   房间开始时间,格式 2013-10-27 11:11
        duration    Y   房间时长,单位小时, 可选值为 1 , 2, 3,4,5
        roomType    Y   房间类型。 可选值为 1,2,8。 “1” 表示 1v1 课程,“2”表示 1vn 课程, "4"表示小班flash课程(需先申请该权限), "8"表示小班客户端(需先申请该权限)
        '''
        url = self.get_url('v3/room/create')
        if duration not in (1, 2, 3, 4, 5):
            raise exceptions.DuobeiSDKInvalidParamException('duration not valid')
        # 东八区注意
        starttime = arrow.get(starttime).format('YYYY-MM-DD HH:mm')
        room_type = constants.RoomType(room_type).value
        timestamp = self.get_now_timestamp()
        params = {
            'partner': self.partner_id, 'title': title, 'startTime': starttime,
            'duration': duration, 'timestamp': timestamp, 'video': video, 'roomType': room_type,
        }
        response = self.request(url, params, method='post')
        return response

    def room_create_v4(self, title, starttime, length, video=0, room_type=2):
        '''
        创建房间(方式2)
        URL
        https://api.duobeiyun.com/api/v4/room/create

        参数名  必填(Y/N)   说明
        partner Y   合作 id
        sign    Y   加密校验值
        timestamp   Y   从 1970 到现在的时间差的毫秒数, 该时间戳的有效期是 5 分钟
        title   Y   房间标题
        video   Y   是否开启视频。开启视频填1，不开启填0
        startTime   Y   房间开始时间,格式 2013-10-27 11:11
        length  Y   房间时长,单位分钟, 不能小于30分钟 不能大于300分钟
        roomType    Y   房间类型。 可选值为 1, 2, 4, 8。 “1” 表示 1v1 课程,“2”表示 1vn 课程, "4"表示小班flash课程, "4"表示小班flash课程(需先申请该权限), "8"表示小班客户端(需先申请该权限)
        '''
        url = self.get_url('v4/room/create')
        length = int(length)
        if length < 30 or length > 300:
            raise exceptions.DuobeiSDKInvalidParamException('length not valid')
        # 东八区注意
        starttime = arrow.get(starttime).format('YYYY-MM-DD HH:mm')
        timestamp = self.get_now_timestamp()
        room_type = constants.RoomType(room_type).value
        params = {
            'partner': self.partner_id, 'title': title, 'startTime': starttime,
            'length': length, 'timestamp': timestamp, 'video': video, 'roomType': room_type,
        }
        response = self.request(url, params, method='post')
        return response

    def room_update_title(self, roomid, title):
        '''
        更新房间标题
        URL
        https://api.duobeiyun.com/api/v3/room/update/title

        参数名  必填(Y/N)   说明
        partner Y   合作 id
        sign    Y   加密校验值
        timestamp   Y   从 1970 到现在的时间差的毫秒数, 该时间戳的有效期是 5 分钟
        roomId  Y   房间Id
        title   Y   新的房间标题
        '''
        url = self.get_url('v3/room/update/title')
        timestamp = self.get_now_timestamp()
        params = {
            'partner': self.partner_id, 'title': title, 'roomId': roomid, 'timestamp': timestamp
        }
        response = self.request(url, params, method='post')
        return response

    def room_update_time(self, roomid, starttime, duration):
        '''
        修改房间开始时间和时长
        URL
        https://api.duobeiyun.com/api/v3/room/update/time

        参数名  必填(Y/N)   说明
        partner Y   合作 id
        sign    Y   加密校验值
        timestamp   Y   从 1970 到现在的时间差的毫秒数, 该时间戳的有效期是 5 分钟
        roomId  Y   房间的 Id
        startTime   Y   房间开始时间,格式 2013-10-27 11:11
        duration    Y   房间时长,单位小时, 可选值为 1 , 2, 3,4,5
        注意 如果房间的开始时间已经超过了当前时间，则无法修改房间开始时间
        '''
        url = self.get_url('v3/room/update/time')
        timestamp = self.get_now_timestamp()
        # 东八区注意
        starttime = arrow.get(starttime).format('YYYY-MM-DD HH:mm')
        params = {
            'partner': self.partner_id, 'roomId': roomid, 'timestamp': timestamp,
            'startTime': starttime, 'duration': duration,
        }
        response = self.request(url, params, method='post')
        return response

    def room_update_time_v4(self, roomid, starttime, length):
        '''
        修改房间开始时间和时长(方式2)
        URL
        https://api.duobeiyun.com/api/v4/room/update/time

        参数名  必填(Y/N)   说明
        partner Y   合作 id
        sign    Y   加密校验值
        timestamp   Y   从 1970 到现在的时间差的毫秒数, 该时间戳的有效期是 5 分钟
        roomId  Y   房间的 Id
        startTime   Y   房间开始时间,格式 2013-10-27 11:11
        length  Y   房间时长,单位分钟, 不能小于30分钟 不能大于300分钟
        注意 如果房间的开始时间已经超过了当前时间，则无法修改房间开始时间
        '''
        url = self.get_url('v4/room/update/time')
        length = int(length)
        if length < 30 or length > 300:
            raise exceptions.DuobeiSDKInvalidParamException('length not valid')
        timestamp = self.get_now_timestamp()
        # 东八区注意
        starttime = arrow.get(starttime).format('YYYY-MM-DD HH:mm')
        params = {
            'partner': self.partner_id, 'roomId': roomid, 'timestamp': timestamp,
            'startTime': starttime, 'length': length,
        }
        response = self.request(url, params, method='post')
        return response

    def room_enter(self, roomid, uid, nickname, user_role, device_type,
            h5='false', ps_time='', pe_time='', tape='', admin_disable_chat='false'):
        '''
        请求进入房间
        URL
        https://api.duobeiyun.com/api/v3/room/enter

        注意: 使用iframe嵌入，父页面请使用https。在chrome60以及以上版本，若父页面非https，则可能会无法访问麦克风和摄像头。

        最新版本的chrome，64版本，使用iframe加载包含flash的页面时会出现无法获取音视频的问题，解决方法如下: 在加载iframe时增加allow属性，属性值为geolocation; microphone; camera，示例如下 <iframe src="https://api.duobeiyun.com" allow="geolocation; microphone; camera">

        支持请求返回数据的格式
        HTML , 讲座页面的尺寸大小是 1040 * 600。可以针对这个尺寸做自己适合 的嵌入

        HTTP请求方式
        GET >使用拼接好的进教室链接，访问api接口， 将返回html页面，开发人员以iframe的形式嵌入网页中即可。

        提交参数
        参数名  必填(Y/N)   说明
        partner Y   合作 id
        sign    Y   加密校验值
        timestamp   Y   从 1970 到现在的时间差的毫秒数, 该时间戳的有效期是 5 分钟
        uid Y   用户在自己网站上的唯一标识,一定 不能重复
        roomId  Y   房间 id
        nickname    Y   用户在房间内的昵称，不能为空，昵称首尾不能包含空格
        userRole    Y   可选值为1,2,3,4。 值为1时表示以 主讲人身份进入教室，值为2时表示以听众身份进入教室，值为3时表示以隐身监课者身份进入，值为4时表示以房间助教身份进入教室。当请求不加该参 数时默认以听众身份进入
        deviceType  N   可选值1,2. 当不填deviceType时, 会根据userAgent判断用户访问设备, 并返回页面; 值为1时返回PC客户端; 值为2时返回手机端教室
        h5  N   可选值 true,false，用来强制 PC 端使用 H5版回放（课程必须是音频课，浏览器只能使用 chrome、safari）
        psTime  N   回放开始播放时间，相对于实际播放时间，例如：100:20 表示100分钟20秒的时刻开始播放
        peTime  N   回放结束播放时间，相对于实际播放时间，例如：120:23 表示120分钟23秒的时刻开始播放
        tape    N   可选值: true、false 或 1、0。如果值为true则忽略剪辑、忽略指定的时间播放参数，播放未剪辑的回放内容
        adminDisableChat    N   是否允许管理员发言, 默认为false, 允许发言. 只有当userRole=3时, 该参数生效. 可选值: true、false
        '''
        url = self.get_url('v3/room/enter')
        timestamp = self.get_now_timestamp()
        user_role = constants.UserRole(user_role).value
        device_type = constants.DeviceType(device_type).value
        params = {
            'partner': self.partner_id, 'roomId': roomid, 'timestamp': timestamp,
            'uid': uid, 'nickname': nickname, 'userRole': user_role,
            'DeviceType': device_type, 'h5': h5, 'psTime': ps_time, 'peTime': pe_time,
            'tape': tape, 'adminDisableChat': admin_disable_chat
        }
        response = self.request(url, params, method='get', response_format_type='content')
        return response

    def room_detail(self, roomid):
        '''
        查看教室房间详情
        URL
        https://api.duobeiyun.com/api/v3/room/detail
        参数名  必填(Y/N)   说明
        partner Y   合作 id
        sign    Y   加密校验值
        roomId  Y   房间的 Id
        timestamp   Y   从 1970 到现在的时间差的毫秒数, 该时间戳的有效期是 5 分钟
        '''
        url = self.get_url('v3/room/detail')
        timestamp = self.get_now_timestamp()
        params = {
            'partner': self.partner_id, 'roomId': roomid, 'timestamp': timestamp,
        }
        response = self.request(url, params, method='post')
        return response
