#coding:utf-8
from loginController.LoginController import LoginController
from globalAction.TopFrameAction import TopFrameAction
from Pages import FriendHomePage
from Pages import FocusPage
import time
from Pages import WeiboPageCommon
from Pages import SearchPage
class FollowShipControl:

    #关注评论中出现的好友
    def fouces_friend_of_comment(self, webdriver):
        WeiboPageCommon.scroll(weibo.browser)
        time.sleep(3)
        WeiboPageCommon.scroll(weibo.browser)
        time.sleep(3)
        #获得所有微博
        weibo_list = WeiboPageCommon.get_all_weibo(webdriver)
        friend_address_list = []
        for weibo_driver in weibo_list[:9]:
            try:
                url = self.get_weibo_url(weibo_driver)
                if url:
                    friend_address_list.append(url)
            except Exception as e:
                print(e)
        for url in friend_address_list:
            try:
                print url
                self.foucs_friend(url, webdriver)
            except Exception as e:
                print(e)


        print ''

    def foucs_friend(self, url, webdriver):
        webdriver.get(url)
        webdriver.implicitly_wait(10)
        nums = FriendHomePage.get_friend_info(webdriver)
        foucs_nums = nums[0]
        fans_num = nums[1]
        if foucs_nums/fans_num > 0.5:
            FriendHomePage.focus_action(webdriver)
            time.sleep(3)
        else:
            print '不符合要求，不于关注'

    #获取微博某个评论粉丝的微博地址
    def get_weibo_url(self, weibo_driver):
        wei = WeiboPageCommon.weibo_parse(weibo_driver)
        if wei.comment_num > 0:
            WeiboPageCommon.comment_action(weibo_driver)
            comment_list = WeiboPageCommon.comment_list(weibo_driver)
            comment = WeiboPageCommon.comment_parse(comment_list[0])
            url = comment[0]
            return url

    def focuos(self, webdriver):
        TopFrameAction.homeAction(webdriver)
        focus_box = webdriver.find_element_by_id('Pl_Core_T8CustomTriColumn__3')
        focus_box.find_element_by_link_text("关注").click()

if __name__ == '__main__':
    weibo = LoginController('13951640490', 'gongyong505.')
    weibo.login()
    time.sleep(5)
    weibo.browser.get('http://weibo.com/545352510')
    time.sleep(3)
    FriendHomePage.focus_action(weibo.browser)
    FocusPage.next_page_action(weibo.browser)
    f = FollowShipControl()
    f.fouces_friend_of_comment(weibo.browser)
    weibo_list = WeiboPageCommon.get_all_weibo(weibo.browser)
    time.sleep(3)
    for weibo_driver in weibo_list:
        wei = WeiboPageCommon.weibo_parse(weibo_driver)
        if wei.comment_num > 0:
            WeiboPageCommon.comment_action(weibo_driver)
            comment_list = WeiboPageCommon.comment_list(weibo_driver)
            comment = WeiboPageCommon.comment_parse(comment_list[0])
            url = comment[0]
            weibo.browser.get(url)
            FriendHomePage.focus_action(weibo.browser)
            break

    print ''

