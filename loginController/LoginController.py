#coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from commons.CommonConst import *
import pickle
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
    DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.Accept-Language'] = 'zh-CN,zh;q=0.8'
    DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.Connection'] = 'keep-alive'
    DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.Accept-Encoding'] = 'gzip, deflate, sdch'
    DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.Cache-Control'] = 'max-age=0'
    phantomjs_path = "G:\\programeSoftwares\\python2.7\\Scripts\\phantomjs.exe"
    dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36")
    #browser = webdriver.PhantomJS(desired_capabilities=dcap)
    browser = webdriver.PhantomJS(desired_capabilities=dcap,executable_path=phantomjs_path)
        #self.browser = webdriver.PhantomJS(desired_capabilities=dcap
    browser.set_window_size(1920, 1080)
    return browser

def mobile_login(browser, username, passwd):
    print '开始登录'
    PORTAL_URL = 'http://m.weibo.cn'
    browser.get(PORTAL_URL)
    time.sleep(5)
    login_button_box = browser.find_element_by_class_name('action')
    login_button = login_button_box.find_elements_by_tag_name('a')[1]
    login_button.click()
    time.sleep(4)
    return __input_login_info(browser, username, passwd)


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
    return browser

def log_in(browser, username, passwd):
    browser.get('http://weibo.com/')
    time.sleep(5)
    browser.find_element_by_xpath("//a[@node-type='normal_tab']").click()
    browser.find_element_by_xpath("//input[@node-type='username']").send_keys(username)

    time.sleep(1)
    browser.find_element_by_xpath("//input[@node-type='password']").send_keys(passwd)
    browser.find_element_by_xpath("//a[@node-type='submitBtn']").click()
    time.sleep(5)
    print(browser.title)
    pickle.dump(browser.get_cookies(), open('cookie', 'wb'))


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
    browser.get('http://m.weibo.cn/mblog')
    time.sleep(5)
    print '页面标题:'
    print browser.title
    if '我的首页' in browser.title.encode('utf-8'):
        pickle.dump(browser.get_cookies(), open('cookie', 'wb'))

if __name__ == '__main__':
    print ''


