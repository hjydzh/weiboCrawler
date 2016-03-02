#coding:utf-8
import time
from dmo.FansInfo import FansInfo
from commons import CommonConst
from selenium.common.exceptions import NoSuchElementException

#关注和粉丝页面

#返回一页的关注列表信息, 并可以对处理过的fansInfo对象使用func函数，func函数无返回值
def focus_list_one(driver, func):
    focus_list = driver.find_elements_by_xpath("//li[@class='member_li S_bg1']")
    return map(lambda focus : __fans_info_wrapper_func(__focus_parse(focus), func), focus_list)

#返回所有页的关注列表信息,并可以对处理过的fansInfo对象使用func函数，func函数无返回值
def focus_list_all_with_func(driver, func):
    list = focus_list_one(driver, func)
    while next_page(driver):
        list.extend(focus_list_one(driver, func))
    return list

def focus_list_all(driver):
    return focus_list_all_with_func(driver, lambda x:x)

def __fans_info_wrapper_func(fans_info, func):
    func(fans_info)
    return fans_info

#解析关注对象信息
def __focus_parse(focus_driver):
    fans = FansInfo()
    wrapper_driver = focus_driver.find_element_by_xpath(".//a[@node-type='screen_name']")
    fans.id = wrapper_driver.get_attribute('usercard').encode('utf-8')[3:]
    fans.name = wrapper_driver.get_attribute('title').encode('utf-8')
    fans.href = wrapper_driver.get_attribute('href').encode('utf-8')
    fans.driver = focus_driver
    relationship = focus_driver.find_element_by_class_name('statu').text.encode('utf-8')
    if relationship == '互相关注':
       fans.relationship = CommonConst.Const.FOCUS_EACH_OTHER
    else:
        fans.relationship = CommonConst.Const.ME_FOCUS_HIM
    return fans

#取消关注
def cancel_focus(focus_driver, driver):
    focus_driver.find_element_by_xpath(".//a[@action-type='relation_hover']").click()
    focus_driver.find_element_by_xpath(".//a[@action-type='cancel_follow_single']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//a[@action-type='ok']").click()

#如果下一页按钮已经按下，返回true.如果无法按下，说明已经是最后一页，返回false
def next_page(driver):
    try:
        next_driver = driver.find_element_by_xpath("//a[@class='page next S_txt1 S_line1']")
        next_driver.click()
        time.sleep(2)
        return True
    except NoSuchElementException:
        return False
