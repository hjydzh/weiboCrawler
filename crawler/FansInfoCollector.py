#coding:utf-8
import sys
import time
sys.path.append('/home/workspace/webcrawler/weiboCrawler')
from loginController import LoginController
from Pages import FocusFollowPage

class FansInfoCollector:

    def __init__(self, browser):
        self.browser = browser

    def collect(self):
        LoginController.login_by_cookie(self.browser)
        #self.browser.get('http://weibo.com/5579712614/follow')
        #time.sleep(4)
        a = self.browser.find_element_by_xpath("//a[@node-type='mUpload']")
        a.send_keys(open('2.jpg'))
        list = FocusFollowPage.focus_list_all_with_func(self.browser, self.p)
        print('')

    def p(self, fans):
        print fans.name


if __name__ == '__main__':
    crawler = FansInfoCollector(LoginController.get_chrome())
    crawler.collect()

