#coding=utf-8
import datetime
import time
class DateUtils:

    STYLE1 = "%Y%m%d%H%M%S"

    STYLE_MYSQL = "%Y-%m-%d %H:%M:%S"

    STYLE_YMD = "%Y%m"

    @staticmethod
    def now():
        return datetime.datetime.now()

    @staticmethod
    def now_format(style):
        return DateUtils.now().strftime(style)

    @staticmethod
    def date_of_str():
        return DateUtils.now().strftime("%Y%m%d%H%M%S")

    @staticmethod
    def day_now_str(style):
        return DateUtils.now().strftime(style)

    #日期转换成字符串
    @staticmethod
    def date_of_str_format(date, style):
        return date.strftime(style)

    #字符串转换成时间戳
    @staticmethod
    def str_time(time_str, style):
        return  datetime.datetime.strptime(time_str, style)

    #增加指定天数
    @staticmethod
    def add_day(date, day):
        return  date + datetime.timedelta(days=day)

        #减去指定天数
    @staticmethod
    def substract_day(date, day):
        return  date - datetime.timedelta(days=day)

    #减去指定分
    @staticmethod
    def substract_minus(date, minus):
        return  date - datetime.timedelta(minutes=minus)

    #现在时间减去指定分
    @staticmethod
    def substract_minus_by_now(minus):
        return  DateUtils.now() - datetime.timedelta(minutes=minus)

    @staticmethod
    def get_month():
        return DateUtils.now().strftime(DateUtils.STYLE_YMD)
if __name__ == '__main__':
    s = '2014-8-20 15:42'
    STYLE_MYSQL = "%Y-%m-%d %H:%M"
    print DateUtils.str_time(s, STYLE_MYSQL)
