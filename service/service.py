#coding:utf-8
from utils import HttpUtil
import os
import time

def send_weibo(text, url, browser):
    browser.get('http://m.weibo.cn/mblog')
    time.sleep(3)
    browser.find_element_by_id('txt-publisher').send_keys(text)
    open(r'/home/1.jpg', 'wb').write(HttpUtil.request(url))
    browser.find_element_by_class_name('picupload').send_keys(r'/home/1.jpg')
    time.sleep(4)
    browser.find_element_by_link_text('发送').click()
    time.sleep(3)
    os.remove(r'/home/1.jpg')
    print '发送成功'




