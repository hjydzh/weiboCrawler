#coding:utf-8
import sys
sys.path.append('/home/workspace/webcrawler/weiboCrawler')
import time
from service import service
from utils import HttpUtil
from BeautifulSoup import BeautifulSoup
from service import service
from loginController import LoginController
from commons.CommonConst import *
from utils import PasswdUtil

class YuLuCrawler:

    def search(self):
        url = 'http://www.wyl.cc/'
        home_soup = BeautifulSoup(HttpUtil.request(url))
        target_url = home_soup.find(attrs={"class": "entry-title"}).find('a')['href'].encode('utf-8')
        target_soup = BeautifulSoup(HttpUtil.request(target_url))
        content_soup = target_soup.find(attrs={"class": "single-content"}).findAll('p')
        text = content_soup[0].text
        url = content_soup[1].find('a')['href'].encode('utf-8')
        self.__send(text, url)


    def __send(self, text, url):
        passwd_dict = PasswdUtil.get_passwd_dict()
        browser = LoginController.get_browser()
        try:
            service.send_weibo(text, url, LoginController.mobile_login(browser, passwd_dict[Const.WEIBO_USERNAME], passwd_dict[Const.WEIBO_PASSWD]))
        except Exception as e:
            print e
            browser.quit()

    def chick_search(self):
        url = 'http://www.59xihuan.cn/'
        home_soup = BeautifulSoup(HttpUtil.request(url))
        content_soup = home_soup.find(attrs={"class": "pic_text1"})
        text = content_soup.find('p').text
        url = url + content_soup.find('img')['bigimagesrc'].encode('utf-8')
        self.__send(text, url)
        print ''



if __name__ == '__main__':
    crawler = YuLuCrawler()
    crawler.chick_search()
