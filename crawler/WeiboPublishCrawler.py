#coding:utf-
import sys
sys.path.append('/home/workspace/webcrawler/weiboCrawler')
from Pages import WeiboPageCommon
from Pages import HomePage
from strategy import PublishStrategy
from loginController import LoginController
import time
import traceback


class WeiboPublishCrawler:

    def __init__(self, browser):
        self.browser = browser

    def publish(self):
        LoginController.login(self.browser, '2823128008@qq.com', 'a13870093884')
        #WeiboPageCommon.scroll(self.browser)
        time.sleep(4)
        weibo_list =  WeiboPageCommon.get_all_weibo(self.browser)
        weibos = map(lambda weibo_driver:self.__get_webibo_info(weibo_driver), weibo_list)
        #WeiboPageCommon.scroll(self.browser)
        weibos.extend(map(lambda weibo_driver:self.__get_webibo_info(weibo_driver), WeiboPageCommon.get_all_weibo(self.browser)[len(weibo_list):]))
        weibos = filter(lambda w : w is not None , weibos)
        sorted_weibos = PublishStrategy.nums_strategy(weibos)
        WeiboPageCommon.forword_weibo(self.browser, sorted_weibos[0], '')
        print ''

    def __get_webibo_info(self, weibo_driver):
        try:
            author_info = HomePage.show_fans_info(weibo_driver, self.browser)
            weibo = WeiboPageCommon.weibo_parse(weibo_driver)
            weibo.author_info = author_info
        except :
            traceback.print_exc()
            return None
        return weibo


if __name__ == '__main__':
    crawler = WeiboPublishCrawler(LoginController.get_browser())
    crawler.publish()
