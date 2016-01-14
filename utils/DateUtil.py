#coding=utf-8
import datetime
import time
from commons import TimeConst

def now():
    return datetime.datetime.now()

#当前时间输出字符串
def now_format(style):
    return now().strftime(style)

#日期转换成字符串
def time_to_str(date, style):
    return date.strftime(style)

def date_of_str():
    return now().strftime(TimeConst.Const.STYLE1)

#字符串转换成时间
def str_to_time(time_str, style):
    return  datetime.datetime.strptime(time_str, style)

#增加指定天数
def add_day(date, day):
    return  date + datetime.timedelta(days=day)

#减去指定天数
def substract_day(date, day):
    return  date - datetime.timedelta(days=day)

#现在时间减去指定分
def substract_minus_by_now(minus):
    return  now() - datetime.timedelta(minutes=minus)

#获取当前年月
def get_month():
    return now().strftime('%Y%m')

#时间字符串转换为时间戳
def str_to_time_time(time_str):
    return time.mktime(time.strptime(time_str,TimeConst.Const.STYLE_MYSQL))

#时间字符串转换为时间戳
def str_to_time_time_style(time_str,style):
    return time.mktime(time.strptime(time_str,style))

if __name__ == '__main__':
    a = date_of_str()
    print str_to_time_time('2016-01-15 00:13:13')