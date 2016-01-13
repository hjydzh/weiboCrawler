#coding:utf-8
import time

#好友微博主页

#关注好友
def focus_friend_action(driver):
    parent = driver.find_element_by_class_name('pf_opt')
    parent.find_element_by_tag_name('a').click()
    print('关注好友')
    driver.implicitly_wait(2)


#返回[关注数，粉丝数，微博数]
def get_friend_info(web_driver):
    return [int(num.text) for num in web_driver.find_element_by_class_name('tb_counter').find_elements_by_tag_name('strong')[:3]]

#关注按钮
def focus_action(webdriver):
    webdriver.find_elements_by_xpath(".//a[@class='t_link S_txt1']")[0].click()
    print('查看好友的关注')
    webdriver.implicitly_wait(5)

#打开好友的关注页面
def focus_url_action(webdriver, user_id):
    webdriver.get('http://weibo.com/p/%s/follow' % user_id)

#打开好友的粉丝页面
def fans_url_action(webdriver, user_id):
    webdriver.get('http://weibo.com/p/%s/follow?relate=fans' % user_id)


#粉丝按钮
def fans_action(webdriver):
    webdriver.find_elements_by_xpath(".//a[@class='t_link S_txt1']")[1].click()
    print('查看他的粉丝')
    webdriver.implicitly_wait(5)

def user_name(webdriver):
    return webdriver.find_element_by_class_name('username').text

#微博按钮
def weibo_action(webdriver):
    webdriver.find_elements_by_xpath(".//a[@class='t_link S_txt1']")[2].click()
    time.sleep(3)

#返回(省，市)
def address(webdriver):
    try:
        address_info = webdriver.find_element_by_xpath(".//em[@class='W_ficon ficon_cd_place S_ficon']").find_element_by_xpath('..').find_element_by_xpath('..').text.encode('utf-8').split(' ')
    except Exception as e:
        print e
        return ('', '')
    country = address_info[0]
    if len(address_info) > 1:
        city = address_info[1]
    else:
        city = ''
    return (country, city)






