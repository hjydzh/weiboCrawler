#coding:utf-8

import urllib2
import urllib
import cookielib


def request(url):
    return urllib2.urlopen(url).read()

def init_opener():
    auth_url = 'https://pay.suning.com/epp-admin/j_security_check.action'
    data={
        "j_username":"",
        "j_password":""
    }
    post_data=urllib.urlencode(data)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
    cookieJar=cookielib.CookieJar()
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
    req=urllib2.Request(auth_url,post_data,headers)
    opener.open(req)
    return opener
 #document.getElementById('ueditor_0').contentWindow.document.getElementsByClassName('view')[0].innerHTML='%s';
def replace_html(s):
    s = s.replace('"','&quot;')
    s = s.replace('&','&amp;')
    s = s.replace('<','&lt;')
    s = s.replace('>','&gt;')
    s = s.replace(' ','&nbsp;')
    return s

def request_post(url, data):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
    post_data=urllib.urlencode(data)
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    req=urllib2.Request(url,post_data,headers)
    return opener.open(req).read()

if __name__ == '__main__':
    print request('http://www.jianshu.com/p/62e9c9173f4c')