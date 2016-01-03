#coding:utf-8
import HomePage
import time
from selenium.webdriver.common.keys import Keys

#我关注的 页面
def visit_focus_page(driver):
    HomePage.visit_home_page(driver)
    time.sleep(5)
    focus_box = driver.find_element_by_class_name('tb_counter')
    focus_box.find_elements_by_tag_name("a")[0].click()
    time.sleep(5)

def search(driver, name):
    search_box = driver.find_element_by_class_name('search_box')
    input_box = search_box.find_element_by_tag_name('input')
    input_box.send_keys(name)
    search_box.find_element_by_tag_name('a').click()

def all_member(driver):
    return driver.find_element_by_class_name("member_box").find_elements_by_tag_name('li')

#取消关注
def cancel_focus(driver):
    members = all_member(driver)
    for member in members:
        cancel_follow_action(member, driver)
        cancel_focus(driver)
        break

#未分组好友
def un_classify_friend_action(driver):
    parent = driver.find_element_by_class_name('lev2_list')
    list_box = parent.find_elements_by_tag_name('li')
    for li in list_box:
        text = li.find_element_by_tag_name('span').text
        if u'未分组' ==  li.find_element_by_tag_name('span').text:
            li.find_element_by_tag_name('a').click()
            time.sleep(3)
            break

#取消关注好友
def cancel_follow_action(member_driver, driver):
    parent = member_driver.find_element_by_class_name('layer_menu_list')
    if u'已关注' == friend_focus_status(member_driver):
        member_driver.find_element_by_class_name('btn_bed').find_elements_by_tag_name('a')[1].click()
        parent.find_elements_by_tag_name('li')[2].find_element_by_tag_name('a').click()
        time.sleep(3)
        wrapper = driver.find_elements_by_class_name("W_layer")
        wrapper[2].find_elements_by_tag_name('a')[1].click()
        time.sleep(3)


#好友关注状态
def friend_focus_status(member_driver):
    parent = member_driver.find_element_by_class_name('statu')
    return parent.find_element_by_class_name('S_txt1').text

#下一页按钮
def next_page_action(webdriver):
    webdriver.find_element_by_xpath(".//a[@class='page next S_txt1 S_line1']").click()
    time.sleep(3)





