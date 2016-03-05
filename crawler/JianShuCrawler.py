#coding=utf-8
import sys
sys.path.append('/home/workspace/webcrawler/weiboCrawler')
from utils import HttpUtil
from BeautifulSoup import BeautifulSoup
from service import service
from loginController import LoginController
from commons.CommonConst import *
from utils import PasswdUtil


def publish_articles():
    url = 'http://www.jianshu.com'
    html = BeautifulSoup(HttpUtil.request(url))
    articles_soup = [ parse_article_soup(article)  for article in html.find(attrs={"class": "article-list thumbnails"}).findAll('li')]
    sorted_articles = sorted(articles_soup, key=lambda articl_soup:articl_soup[0], reverse=True)
    article_body = service.jian_shu_article_retrive(url + sorted_articles[0][1])
    browser = LoginController.get_browser()
    passwd_dict = PasswdUtil.get_passwd_dict()
    send_text = '《%s》 又到每天推荐文章的时候到了，这些都是精选的枕边读物哦，希望大家喜欢@当幸福敲不开门[害羞][害羞][害羞] ' % article_body[0]
    service.send_weibo(send_text, service.txt_to_pic(article_body[1], browser),  LoginController.mobile_login(browser, passwd_dict[Const.WEIBO_USERNAME], passwd_dict[Const.WEIBO_PASSWD]))


def parse_article_soup(soup):
    title =  soup.find(attrs={"class": "title"}).text.encode('utf-8')
    if '简书' in title:
        return (0, '')
    target_soup = soup.find(attrs={"class": "list-footer"}).find('a')
    return (int(target_soup.text.split(' ')[1].encode('utf-8')),target_soup['href'].encode('utf-8') )

if __name__ == '__main__':
    publish_articles()
