#coding:utf-8
from Pages import FriendHomePage
from Pages import SearchPage
from Pages import WeiboPageCommon
from Pages import FriendFoucsPage
from commons.DateUtils import DateUtils

import time
import pickle
class CareerCrawler:

    last_weibo_in_time = True

    un_visited_url_file_name = 'un_visited_url.data'

    visited_url_file_name = 'visited_url.data'

    def __init__(self, webdriver):
        self.webdriver = webdriver

    def init(self):
        with open(self.un_visited_url_file_name, 'r') as file:
            self.un_visited_url = pickle.load(file)
        with open(self.visited_url_file_name, 'r') as file:
            self.visited_url = pickle.load(file)
        map(self.search(self.webdriver), self.un_visited_url)



    #搜索一个粉丝，fans_driver为粉丝主页
    def search(self, fans_driver):
        print(self.visited_url)
        try:

            if fans_driver.current_url in self.visited_url:
                print fans_driver.current_url
                print('存在')
                return
            self.visited_url.add(fans_driver.current_url)
            address = FriendHomePage.address(fans_driver)
            username = FriendHomePage.user_name(fans_driver)
            if not '江苏' in address[0]:
                print('不在江苏')
                print(address[0])
                print(fans_driver.current_url)
                return
            if self.focus_check(fans_driver, address):
                FriendHomePage.focus_friend_action(fans_driver)
            fans_url = []
            while self.last_weibo_in_time:
                fans_url.extend(self.weibo_list(fans_driver,username))
                try:
                    WeiboPageCommon.next_page_action(fans_driver)
                except Exception as e:
                    print(e)
                    break



            print ''
            #搜索关注列表
            FriendHomePage.focus_action(fans_driver)
            focus_fans_list = FriendFoucsPage.fans_list_parsed(fans_driver)
            #搜索粉丝列表
            FriendFoucsPage.fans_action(fans_driver)
            fans_list = FriendFoucsPage.fans_list_parsed(fans_driver)
            focus_fans_list.extend(fans_list)
            url_list = []
            for fans in focus_fans_list:
                if '江苏' in fans.address[0]:
                    url_list.append(fans.href)

            fans_url.extend(url_list)
            fans_url = set(fans_url)
            self.un_visited_url = fans_url
            with open(self.un_visited_url_file_name, 'w') as file:
                pickle.dump(self.un_visited_url, file)
                print '保存未访问url'
            for url in fans_url:
                fans_driver.get(url)
                fans_driver.implicitly_wait(10)
                self.search(fans_driver)
                self.visited_url.add(url)
                self.un_visited_url.remove(url)
            with open(self.visited_url_file_name, 'w') as file:
                pickle.dump(self.visited_url, file)
                print '保存访问url'


        except Exception as e:
            print e
            return

    #保证到底部
    def weibo_list(self, webdriver, username):
        fans_url = []
        WeiboPageCommon.scroll(webdriver)
        WeiboPageCommon.scroll(webdriver)
        #搜索评论
        weibo_list = [ WeiboPageCommon.weibo_parse_simple(weibo)  for weibo in WeiboPageCommon.get_all_weibo(webdriver)]
        search_weibo_list = filter(self.time_check, weibo_list)
        for weibo in search_weibo_list:
            fans_href = self.comment_fans_href(weibo.weibo_driver, username)
            fans_url.extend(fans_href)
        return  fans_url

    #是否允许关注好友
    def focus_check(self, fans_driver, address):
        fans_info = FriendHomePage.get_friend_info(fans_driver)
        focus_num = fans_info[0]
        fans_num = fans_info[1]
        weibo_num = fans_info[2]
        return focus_num < 500 and fans_num < 5000 and weibo_num > 20 and '南京' in address[1]

    #如果是江苏省，则允许搜索
    def search_check(self, fans_driver):
        address = FriendHomePage.address(fans_driver)
        return '江苏' in address[0]

    #只搜索半年内微博的评论数.自然评论数不能为0
    def time_check(self, weibo):
        time = weibo.time
        interval = 180
        weibo_before_time = DateUtils.substract_day(DateUtils.now(), interval) < time
        self.last_weibo_in_time = weibo_before_time
        return  weibo_before_time and weibo.comment_num > 0

    #获取一个微博所有评论的粉丝地址
    def comment_fans_href(self, weibo_driver, username):
        comment_fans_list = WeiboPageCommon.parsed_comment_fans(weibo_driver)
        fans_url_list = []
        for fan in comment_fans_list:
            if fan[2] != username:
                fans_url_list.append(fan[0])
        return fans_url_list

if __name__ == '__main__':
    #un_visited_url = set('http://weibo.com/u/730120310')
    #with open('un_visited_url.data', 'w') as file:
       #pickle.dump(un_visited_url, file)
    #with open('visited_url.data', 'w') as file:
        #pickle.dump(set(), file)
    #weibo = LoginController('13951640490', 'gongyong505.')
    weibo = LoginController('junyuhuangwan@sina.com', 'weibojun@123')
    weibo.login()
    weibo.browser.implicitly_wait(30)
    weibo.browser.get('http://weibo.com/u/2062931202')
    weibo.browser.implicitly_wait(30)
    crawler = CareerCrawler(weibo.browser)
    crawler.init()
    crawler.search(weibo.browser)






