#  Copyright (c) 2019. YH Software Inc. Corp.

# Author: Jiaheng Gary Li
# @Time : 5/8/2019 8:57 AM
# Project: 
# Name: my_datetime
# Description:

# 标准库datetime

# datetime模块

import datetime

# datetime 类
#   类方法
#       today() 返回本地时区当前时间的datetime对象
#       now(tz=None) 返回当前时间的datetime对象，时间到微秒，如果tz为None，返回和today()一样
#       utcnow()没事时区的当前时间
#       fromtimestamp(timestamp, tz=None)从一个时间戳返回一个datetime对象
#   datetime对象
#       timestamp()返回一个到微秒的时间戳。
#           时间戳：格林威治时间1970年1月1日0点到现在的秒数
#       构造方法 datetime.datetime(2016,12,6,13,34,43,82398)
#       year, month, day, hour, minute, second, microsecond, 取datetime对象的年月日时分秒及微秒
#       weekday() 返回星期的天，周一0，周日6
#       isoweekday() 返回星期的天，周一1，周日7
#       date() 返回日期date对象
#       time() 返回时间time对象


print(datetime.datetime.now())
print(datetime.datetime.utcnow())


#   日期格式化
#       类方法 strptime(date_string, format), 返回datetime对象
#       对象方法 strftime(format), 返回字符串
#       字符串format函数格式化
dt = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(dt.strftime("%y-%m-%d %H:%M:%S"))
print("{0:%Y}/{0:%m}/{0:%d} {0:%H}:{0:%M}:{0:%S}".format(dt))


#   timedelta对象
#       datetime2 = datetime1 + timedelta
#       datetime2 = datetime1 - timedelta
#       timedelta = datetime1 - datetime2
#       构造方法
#       datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0,minutes=0,hours=0,weeks=0)
#       year = datetime.timedelta(days = 365)
#       total_seconds()返回时间差的总秒数


# 标准库time

import time

# time.sleep(secs) 将调用线程挂起指定的秒数


