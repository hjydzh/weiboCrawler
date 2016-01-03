#coding:utf-8
import time
#私信页面

#获得未分组好友
def get_other_fans_list(webdriver):
    time.sleep(2)
    fans_list_driver = webdriver.find_elements_by_xpath("//div[@class='webim_contacts_group mt10']")[-1]
    fans_list_driver.find_element_by_xpath(".//a[@class='group_title_cont S_txt1']").click()
    time.sleep(2)
    return fans_list_driver.find_elements_by_tag_name('li')


#输入消息
def __input_fans_msg(webdriver, msg):
    webdriver.find_element_by_tag_name('textarea').send_keys(msg)

#发送
def send_fans_msg(webdriver, msg):
    __input_fans_msg(webdriver, msg)
    webdriver.find_element_by_xpath(".//a[@action-type='submit']").click()

#获取所有好友列表
def get_fans_list(webdriver):
    return  webdriver.find_elements_by_xpath(".//dd[@class='mod_info S_line1']")

