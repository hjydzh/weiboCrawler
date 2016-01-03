#coding:utf-8
import time
from dmo.FansInfo import FansInfo

#好友的关注页面

#下一页按钮
def next_page_action(webdriver):
    webdriver.find_element_by_xpath(".//a[@class='page next S_txt1 S_line1']").click()
    print '下一页'
    time.sleep(3)

#“他的关注”按钮
def focus_action(webdriver):
    webdriver.find_elements_by_xpath(".//a[@action-type='nav_lev']")[0].click()
    print '查看他的关注'
    webdriver.implicitly_wait(30)

#“他的粉丝”按钮
def fans_action(webdriver):
    webdriver.find_elements_by_xpath(".//a[@action-type='nav_lev']")[1].click()
    print '查看他的粉丝'
    webdriver.implicitly_wait(30)

#好友列表
def fans_list(webdriver):
    fans = webdriver.find_elements_by_xpath(".//li[@class='follow_item S_line2']")
    return fans

#解析后的好友列表
def fans_list_parsed(webdriver):
    list = []
    for i in range(4):
        fans = fans_list(webdriver)
        try:
            list.extend(map(fans_parse, fans))
        except Exception as e:
            print e
        try:
            next_page_action(webdriver)
        except Exception as e:
            print e
            return list
    return list

def fans_parse(fans_driver):
    print('解析关注中的好友列表')
    href = fans_driver.find_element_by_class_name('S_txt1').get_attribute('href')
    nums_driver = fans_driver.find_elements_by_class_name('count')
    focus_num = nums_driver[0].text
    fans_num = nums_driver[1].text
    weibo_num = nums_driver[2].text
    address = fans_driver.find_element_by_class_name('info_add').find_element_by_tag_name('span').text.encode('utf-8').split(' ')
    country = address[0]
    if len(address) > 1:
        city = address[1]
    else:
        city = ''
    address = (country, city)
    fans = FansInfo()
    fans.href = href
    fans.focus_num = focus_num
    fans.fans_num = fans_num
    fans.weibo_num = weibo_num
    fans.address = address
    return fans


