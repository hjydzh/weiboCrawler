#coding:utf-8
#粉丝信息详情
class FansInfo:
    id = ''
    name = ''
    gender = ''
    href = ''
    focus_num = 0;
    fans_num = 0
    weibo_num = 0
    edu = ''
    company = ''
    address = ()
    #存放需要的driver
    driver = None
    #和我的关系,0为互相关注，1为我关注了他，2为他关注了我
    relationship = None
