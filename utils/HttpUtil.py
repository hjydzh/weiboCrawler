#coding:utf-8
import urllib2

def request(url):
    return urllib2.urlopen(url).read()
