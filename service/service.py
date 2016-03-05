#coding:utf-8
from utils import HttpUtil
import os
import time
import json
from BeautifulSoup import BeautifulSoup
from loginController import LoginController
import cgi
from commons.CommonConst import *
from utils import PasswdUtil

def send_weibo(text, url, browser):
    browser.get('http://m.weibo.cn/mblog')
    time.sleep(3)
    browser.find_element_by_id('txt-publisher').send_keys(text.decode('utf-8'))
    open(r'/home/1.jpg', 'wb').write(HttpUtil.request(url))
    browser.find_element_by_class_name('picupload').send_keys(r'/home/1.jpg')
    time.sleep(4)
    browser.find_element_by_link_text('发送').click()
    time.sleep(10)
    os.remove(r'/home/1.jpg')
    print '发送成功'

#把文本转换成图片，长微博形式
def txt_to_pic(txt, browser):
    url = 'http://www.changweibo.com/'
    js ="""document.getElementById('ueditor_0').contentWindow.document.getElementsByClassName('view')[0].innerHTML='%s';
    """ %  str(txt).replace('\n', '<br>').replace('\'', '"')
    browser.get(url)
    time.sleep(5)
    #button = browser.find_element_by_id("edui111_body")
    #button.click()
    browser.execute_script(js)
    time.sleep(3)
    browser.find_element_by_xpath("//a[@class='btn btn-success btn-lg']").click()
    time.sleep(10)
    browser.switch_to_frame('ueditor_0')
    html = browser.page_source
    soup = BeautifulSoup(html)
    data={
        "reserve_check":1,
        "text":"",
        "html":soup.find('body')
    }
    url = 'http://www.changweibo.com/convert_changweibo_com.php'
    response = HttpUtil.request_post(url, data)
    img_url =  json.loads(response)['image_url']
    print(img_url)
    return img_url


#返回简书文章内容和标题
def jian_shu_article_retrive(url):
    html = HttpUtil.request(url)
    content_soup = BeautifulSoup(html, fromEncoding="utf-8").find(attrs={"class": "article"})
    title = content_soup.find(attrs={"class": "title"}).text.encode('utf-8')
    content = content_soup.find(attrs={"class": "show-content"})
    return (title, content)


if __name__ == '__main__':
    article = jian_shu_article_retrive('http://www.jianshu.com/p/6b36ae903883')
    browser = LoginController.get_browser()
    passwd_dict = PasswdUtil.get_passwd_dict()
    send_weibo(article[0], txt_to_pic(article[1], browser),  LoginController.mobile_login(browser, passwd_dict[Const.WEIBO_USERNAME], passwd_dict[Const.WEIBO_PASSWD]))
    #print txt_to_pic([1], LoginController.get_chrome())
    #print(jian_shu_article_retrive('http://www.jianshu.com/p/f3237b61d54a'))

