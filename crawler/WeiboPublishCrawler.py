#coding:utf-8
import sys
sys.path.append('/home/workspace/webcrawler/weiboCrawler')
from Pages import WeiboPageCommon
from Pages import FriendHomePage
from strategy import PublishStrategy
from loginController import LoginController
import time
import traceback
from dmo.FansInfo import FansInfo
from service import service
from commons.CommonConst import *
from utils import PasswdUtil

class WeiboPublishCrawler:

    def __init__(self, browser):
        self.browser = browser

    def publish(self):
        self.browser.set_page_load_timeout(120)
        passwd_dict = PasswdUtil.get_passwd_dict()
        LoginController.mobile_login(self.browser, passwd_dict[Const.WEIBO_USERNAME], passwd_dict[Const.WEIBO_PASSWD])
        #LoginController.login_by_cookie(self.browser)
        print('等待4s,滚动屏幕')
        WeiboPageCommon.scroll(self.browser)
        time.sleep(4)
        WeiboPageCommon.scroll(self.browser)
        time.sleep(4)
        WeiboPageCommon.scroll(self.browser)
        time.sleep(4)
        print('等待结束')
        try:
            weibo_list =  WeiboPageCommon.get_all_weibo(self.browser)
        except:
            traceback.print_exc()
            self.browser.get('http://weibo.com/')
            time.sleep(4)
            weibo_list =  WeiboPageCommon.get_all_weibo(self.browser)
        print('需要解析的微博数目:' + str(len(weibo_list)))
        weibos = map(lambda weibo_driver:self.__get_webibo_info(weibo_driver), weibo_list)
        #weibos.extend(map(lambda weibo_driver:self.__get_webibo_info(weibo_driver), WeiboPageCommon.get_all_weibo(self.browser)[len(weibo_list):]))
        weibos = filter(lambda w : w is not None , weibos)
        #打开新的选项卡
        #self.browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
        #self.browser.execute_script("window.open('http://weibo.com/','_blank');")
        #wins = self.browser.window_handles
        #self.browser.switch_to_window(wins[1])
        #self.browser.set_window_size(1366, 768)
        map(lambda weibo:self.__get_weiboer_info(weibo), weibos)
        #self.browser.switch_to_window(wins[0])
        sorted_weibos = PublishStrategy.nums_strategy(weibos)
        WeiboPageCommon.forword_by_comment(self.browser, sorted_weibos[0])
        self.browser.close()
        self.browser.quit()
        print ''

    def __get_webibo_info(self, weibo_driver):
        try:
            #author_info = HomePage.show_fans_info(weibo_driver, self.browser)
            weibo = WeiboPageCommon.weibo_and_comment_parse(weibo_driver)
            #weibo.author_info = author_info
        except :
            traceback.print_exc()
            return None
        return weibo

    #获取微博用户信息
    def __get_weiboer_info(self, weibo):
        try:
            print('访问:'),
            print(weibo.author_url)
            self.browser.get(weibo.author_url)
            time.sleep(4)
            info = FriendHomePage.get_friend_info(self.browser)
            fans_info = FansInfo()
            fans_info.focus_num = info[0]
            fans_info.fans_num = info[1]
            fans_info.weibo_num = info[2]
            weibo.author_info = fans_info
            pass
        except Exception as e:
            pass


if __name__ == '__main__':
    crawler = WeiboPublishCrawler(LoginController.get_browser())
    try:
        crawler.publish()
    except:
        crawler.browser.quit()