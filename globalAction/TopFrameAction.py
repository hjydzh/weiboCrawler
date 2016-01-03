#coding:utf-8

def homeAction(driver):
    parent = driver.find_element_by_class_name('gn_nav')
    parent.find_element_by_class_name('gn_name').click()
