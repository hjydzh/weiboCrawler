#coding:utf-8
import sys
sys.path.append('/home/workspace/webcrawler/weiboCrawler')
from service import service
from loginController import LoginController
from utils import PasswdUtil
from utils import  DateUtil
from  commons.TimeConst import *

def search():
    date = DateUtil.time_to_str(DateUtil.substract_day(DateUtil.now(), 1), Const.STYLE_YYMMDD)
    txt = '又到了推荐极具视觉冲击图片的时刻了[微笑][微笑] @当幸福敲不开门 '
    url = 'http://freepic.wetu.me/preview/%s%s.jpg'
    browser = LoginController.get_browser()
    passwd_dict = PasswdUtil.get_passwd_dict()
    LoginController.mobile_login(browser, passwd_dict[Const.WEIBO_USERNAME], passwd_dict[Const.WEIBO_PASSWD])
    service.send_weibo_pics(txt, [url % (date, 'i'), url % (date, 'p')], browser)

if __name__ == '__main__':
    search()