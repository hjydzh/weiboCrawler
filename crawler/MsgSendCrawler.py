#coding:utf-8
from Pages import WeiboPageCommon
from Pages import MsgPage
from loginController import LoginController
import pickle
import time


class MsgSendCrawler:

    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd

    def search(self):
        driver = LoginController.get_firfox()
        LoginController.login(driver, self.name, self.passwd)
        driver.get('http://weibo.com/messages?topnav=1&wvr=6')
        list = MsgPage.get_other_fans_list(driver)
        list[0].click()
        list = MsgPage.get_other_fans_list(driver)
        for friend in list:
            friend.click()
            MsgPage.send_fans_msg(driver, u'hello')
            time.sleep(1)
        driver.get('http://weibo.com/duzijian?is_hot=1')
        weibo_list = [ WeiboPageCommon.weibo_parse(weibo)  for weibo in WeiboPageCommon.get_all_weibo(driver)]
        print ''

if __name__ == '__main__':
    crawler = MsgSendCrawler('2823128008@qq.com', 'a13870093884')
    crawler.search()
