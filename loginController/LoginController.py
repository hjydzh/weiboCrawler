#coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from commons.CommonConst import *
import pickle
import os
from selenium.common.exceptions import TimeoutException

def get_chrome():
    profile_dir=r"C:\Users\junyu\AppData\Local\Google\Chrome\User Data"
    options = webdriver.ChromeOptions()
    #options.add_argument("user-data-dir="+os.path.abspath(profile_dir))
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    return webdriver.Chrome('G:/lessUsedTools/browser/chrome/chromedriver.exe',chrome_options=options)

def get_firfox():
    binary = FirefoxBinary('G:/lessUsedTools/browser/firefox/firefox.exe')
    browser = webdriver.Firefox(firefox_binary=binary)
    return browser


def get_browser():
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    phantomjs_path = Const.PHANTOMJS_PATH
    #phantomjs_path = "G:\\programeSoftwares\\python2.7\\Scripts\\phantomjs.exe"
    dcap["phantomjs.page.settings.userAgent"] = (
            #"Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25"
            #"Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25"
            #"Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25"
            #"Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4"
            #"Mozilla/5.0 (Linux; U; Android 4.2.1; zh-CN; VOTO X2 Build/JOP40D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.8.9.457 U3/0.8.0 Mobile Safari/533.1"
            #"Mozilla/5.0 (iPhone; U; ru; CPU iPhone OS 4_2_1 like Mac OS X; ru) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5"
            #"Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25"
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
    )
    browser = webdriver.PhantomJS(desired_capabilities=dcap,executable_path=phantomjs_path)
        #self.browser = webdriver.PhantomJS(desired_capabilities=dcap)
    browser.set_window_size(1366, 768)
    return browser

def mobile_login(browser, username, passwd):
    print '开始登录'
    PORTAL_URL = 'http://m.weibo.cn'
    browser.get(PORTAL_URL)
    login_button_box = browser.find_element_by_class_name('action')
    login_button = login_button_box.find_elements_by_tag_name('a')[1]
    login_button.click()
    time.sleep(4)
    __input_login_info(browser, username, passwd)


    #登陆
def __input_login_info(browser, username, passwd):
    print '输入登录信息'
    username_driver = browser.find_element_by_id('loginName')
    username_driver.send_keys(username)
    passwd_driver = browser.find_element_by_id('loginPassword')
    passwd_driver.send_keys(passwd)
    submit_box = browser.find_element_by_id('loginAction')
    submit_box.click()
    print '登录成功'
    time.sleep(5)
    browser.get('http://weibo.com')
    time.sleep(5)

def log_in(browser, username, passwd):
    browser.get('http://weibo.com/')
    #time.sleep(5)
    browser.find_element_by_xpath("//input[@node-type='username']").send_keys(username)
    browser.find_element_by_xpath("//input[@node-type='password']").send_keys(passwd)
    #browser.find_element_by_xpath("//a[@node-type='submitBtn']").click()
    #time.sleep(5)
    cookies = browser.get_cookies()
    pickle.dump(cookies, open('cookie', 'wb'))
    browser.get('http://weibo.com/')

def login_by_cookie(browser):
    print '开始登录'
    try:
        browser.get('http://weibo.com/')
    except TimeoutException:
        print '页面加载超时，停止加载'
        browser.execute_script('window.stop()')

    browser.execute_script('window.stop()')
    print('登录成功')
    time.sleep(5)
    browser.execute_script('window.stop()')
    browser.delete_all_cookies()
    print('删除原来cookies')
    for cookie in pickle.load(open('cookie')):
        try:
            browser.add_cookie(cookie)
        except:
            pass
    print('添加历史cookies')
    browser.get('http://weibo.com/')
    time.sleep(5)
    print '页面标题:'
    print browser.title

if __name__ == '__main__':
    print ''


