#coding:utf-8
#搜索主页
from dmo.FansInfo import FansInfo

#所有好友列表
def person_list(webdriver):
    list =  webdriver.find_elements_by_xpath(".//div[@class='list_person clearfix']")
    return list

def person_info_parse(person_driver):
    name = person_driver.find_element_by_class_name('person_name').text
    href = person_driver.find_element_by_class_name('person_addr').find_element_by_class_name('W_linkb').text
    person_addr_driver = person_driver.find_element_by_class_name('person_addr').find_elements_by_tag_name('span')
    gender = person_addr_driver[0].get_attribute('title')
    address = person_addr_driver[1].text.encode('utf-8').split('，')[1]
    person_num_driver = person_driver.find_element_by_class_name('person_num').find_elements_by_tag_name('a')
    focus_num = int(person_num_driver[0].text)
    fans_num = int(person_num_driver[1].text)
    weibo_num = int(person_num_driver[2].text)
    infos = info_parse(person_driver)
    company = infos.get('职业信息')
    edu = infos.get('教育信息')
    person_info = FansInfo()
    person_info.name = name
    person_info.address = address
    person_info.company = company
    person_info.edu = edu
    person_info.gender = gender
    person_info.href = href
    person_info.focus_num = focus_num
    person_info.fans_num = fans_num
    person_info.weibo_num = weibo_num
    person_info.focus_action = person_driver.find_element_by_class_name('person_adbtn').find_elements_by_tag_name('a')
    return person_info

def info_parse(webdriver):
    person_label_driver_list = webdriver.find_elements_by_class_name('person_label')
    infos = {}
    for person_label_driver in person_label_driver_list:
        info = person_label_driver.text.encode('utf-8').split('：')
        infos[info[0]] = info[1]
    return infos

def next_page_action(webdriver):
    webdriver.find_element_by_xpath(".//a[@class='page next S_txt1 S_line1']").click()



