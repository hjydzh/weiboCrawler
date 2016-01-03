#coding:utf-8
#个人微博主页
import time
from selenium.webdriver.common.action_chains import ActionChains
from dmo.FansInfo import FansInfo

def visit_home_page(webdriver):
    parent = webdriver.find_element_by_class_name('gn_nav')
    parent.find_element_by_class_name('gn_name').click()

def focus(webdriver):
    focus_box = webdriver.find_element_by_id('Pl_Core_T8CustomTriColumn__3')
    focus_box.find_element_by_link_text("关注").click()

def msg_action(webdriver):
    webdriver.find_element_by_xpath(".//a[@node-type='msg']").click()

#鼠标悬停在头像上面，显示博主信息
def show_fans_info(weibo_driver, webdriver):
    img_driver = weibo_driver.find_element_by_xpath(".//div[@class='WB_face W_fl']").find_element_by_tag_name('img')
    ActionChains(webdriver).move_to_element(img_driver).perform()
    webdriver.implicitly_wait(4)
    fans_info = FansInfo()
    fans_info_driver = webdriver.find_element_by_class_name('layer_personcard')
    fans_nums_info_driver = fans_info_driver.find_element_by_class_name('c_count').find_elements_by_tag_name('em')
    print fans_nums_info_driver[0].text.encode('utf-8').strip()
    fans_info.focus_num = int(fans_nums_info_driver[0].text.encode('utf-8').strip())
    fans_info.fans_num = fans_nums_info_driver[1].text.encode('utf-8')
    if '万' in fans_info.fans_num:
        fans_info.fans_num = int(fans_info.fans_num.strip()[:-3] + '0000')
    else:
        fans_info.fans_num = int(fans_info.fans_num.strip())
    fans_info.weibo_num = int(fans_nums_info_driver[2].text.encode('utf-8').strip())
    fans_info.name = fans_info_driver.find_element_by_class_name('W_f14').get_attribute('title').encode('utf-8')
    fans_info.gender = fans_info_driver.find_element_by_tag_name('em').get_attribute('title').encode('utf-8')
    return fans_info

