#coding:utf-8
from dmo.Weibo import Weibo
import time
from commons.DateUtils import DateUtils
from dmo.Comment import Comment
#任何页面的微博主体页

#点击“评论”
def __comment_action(weibo):
    driver = weibo.find_element_by_xpath(".//a[@action-type='fl_comment']")
    driver.click()
    time.sleep(2)

#返回所有解析过的评论
def __parsed_comment_fans(weibo_driver):
    __comment_action(weibo_driver)
    time.sleep(1)
    return [ __comment_parse(comment) for comment in __comment_list(weibo_driver)]

#获得微博的评论
def __comment_list(weibo_driver):
    return weibo_driver.find_elements_by_xpath(".//div[@class='list_li S_line1 clearfix']")

#解析一条评论，返回(发表评论的地址和评论,名字)
def __comment_parse(comment_driver):
    print('解析一条评论')
    comment = Comment()
    comment_text_list = comment_driver.find_element_by_class_name('WB_text').find_elements_by_tag_name('a')
    comment.fnas_url = comment_text_list[0].get_attribute('href')
    comment.fans_name = comment_text_list[0].text
    good_nums = comment_driver.find_element_by_xpath(".//span[@node-type='like_status']").text.encode('utf-8').strip()
    if good_nums == '':
        comment.good_nums = 0
    else:
        comment.good_nums = int(good_nums)
    comment.comment = __comment_text_filter(comment_driver.text.encode('utf-8').split('：')[1].split('回复')[0]).strip()
    comment.time = time_parse(comment_driver.find_element_by_xpath(".//div[@class='WB_from S_txt2']").text.encode('utf-8'))
    return comment

#解析评论文本
def __comment_text_filter(comment_text):
    if '@' in comment_text:
        return ''
    return comment_text.split('//@')[0].replace('举报', '')

#解析一条微博
def weibo_parse(weibo_driver):
    print('解析一条微博')
    try:
        #自己微博就不会有
        weibo_info = weibo_driver.find_element_by_class_name('WB_info').find_element_by_tag_name('a')
        weibo_author = weibo_info.text.encode('utf-8')
        weibo_href = weibo_info.get_attribute('href')
    except:
        weibo_author = ''
        weibo_href = ''
    comment = weibo_driver.find_element_by_xpath(".//div[@node-type='feed_list_content']").text.encode('utf-8')
    comment_handled = __comment_text_filter(comment)
    nums_driver = weibo_driver.find_element_by_class_name('WB_feed_handle')
    fordward_num  = nums_driver.find_element_by_xpath(".//span[@node-type='forward_btn_text']").text[3:].encode('utf-8')
    comment_num = nums_driver.find_element_by_xpath(".//span[@node-type='comment_btn_text']").text[3:].encode('utf-8')
    good_num = nums_driver.find_element_by_xpath(".//span[@node-type='like_status']").text.encode('utf-8')
    forward_weibo_list = weibo_driver.find_elements_by_xpath(".//div[@node-type='feed_list_forwardContent']")
    weibo_time = weibo_driver.find_element_by_xpath(".//a[@node-type='feed_list_item_date']").text.encode('utf-8')
    weibo = Weibo()
    if forward_weibo_list:
        try:
            forward_weibo = __inner_weibo_parse(forward_weibo_list[0])
            weibo.is_forward = True
        except Exception as e:
            print e
            forward_weibo = None
    else:
        forward_weibo = None
    weibo.author_name = weibo_author
    weibo.author_url = weibo_href
    weibo.comment = comment_handled
    weibo.time = time_parse(weibo_time)
    weibo.weibo_driver = weibo_driver
    if fordward_num:
        weibo.forward_num = int(fordward_num)
    if comment_num:
        weibo.comment_num = int(comment_num)
    if good_num:
        weibo.good_num = int(good_num)
    weibo.fordward_weibo = forward_weibo
    weibo.comment_list = __parsed_comment_fans(weibo_driver)
    return weibo

#简单解析一条微博(解析内容并不多)
def weibo_parse_simple(weibo_driver):
    fordward_num  = weibo_driver.find_element_by_xpath(".//span[@node-type='forward_btn_text']").text[3:].encode('utf-8')
    comment_num = weibo_driver.find_element_by_xpath(".//span[@node-type='comment_btn_text']").text[3:].encode('utf-8')
    good_num = weibo_driver.find_element_by_xpath(".//span[@node-type='like_status']").text.encode('utf-8')
    weibo_time = weibo_driver.find_element_by_xpath(".//a[@node-type='feed_list_item_date']").text.encode('utf-8')
    weibo = Weibo()
    weibo.time = time_parse(weibo_time)
    weibo.weibo_driver = weibo_driver
    if fordward_num:
        weibo.forward_num = fordward_num
    if comment_num:
        weibo.comment_num = comment_num
    if good_num:
        weibo.good_num = good_num
    return weibo

#解析微博中转发的微博
def __inner_weibo_parse(weibo_driver):
    weibo_info = weibo_driver.find_element_by_class_name('WB_info').find_element_by_tag_name('a')
    weibo_author = weibo_info.text[1:].encode('utf-8')
    weibo_href = weibo_info.get_attribute('href')
    comment = weibo_driver.find_element_by_class_name('WB_text').text.encode('utf-8')
    info_list = weibo_driver.find_elements_by_tag_name('li')
    fordward_num = info_list[-3].text[3:].encode('utf-8')
    comment_num = info_list[-2].text[3:].encode('utf-8')
    good_num = info_list[-1].text.encode('utf-8')
    weibo = Weibo()
    weibo.author_name = weibo_author
    weibo.author_url = weibo_href
    weibo.comment = comment
    if fordward_num:
        weibo.forward_num = fordward_num
    if comment_num:
        weibo.comment_num = comment_num
    if good_num:
        weibo.good_num = good_num
    weibo.is_forward = False
    return weibo

#获得所有微博
def get_all_weibo(webdriver):
     print '获取所有微博列表'
     weibo_list = webdriver.find_element_by_xpath("//div[@node-type='homefeed']").find_elements_by_xpath(".//div[@action-type='feed_list_item']")
     print '获取列表成功'
     return weibo_list

def scroll(driver):
    #将页面滚动条拖到底部
    js="var q=document.body.scrollTop=10000"
    driver.execute_script(js)
    time.sleep(3)

#解析微博时间
def time_parse(time_str):
    if '分钟前' in time_str:
        time_str = time_str.split('分钟前')[0]
        weibo_time = DateUtils.substract_minus_by_now(int(time_str))
    elif '今天 ' in time_str:
        time_str = time_str.split('今天 ')[1]
        weibo_style = '%Y-%m-%d '
        day = DateUtils.now_format(weibo_style)
        time = day + time_str + ':00'
        weibo_time = DateUtils.str_time(time, DateUtils.STYLE_MYSQL)
    elif '2015' in time_str or '2014' in time_str or '2013' in time_str or '2012' in time_str or '2011' in time_str:
        style = "%Y-%m-%d %H:%M"
        weibo_time = DateUtils.str_time(time_str, style)
    elif '秒前' in time_str:
        style = "%Y-%m-%d %H:%M"
        weibo_time = DateUtils.day_now_str(style)
    else:
        weibo_style =  '%Y年%m月%d日 %H:%M:%S'
        time_str = str(DateUtils.now().year) + '年' + time_str + ':00'
        weibo_time = DateUtils.str_time(time_str, weibo_style)
    return weibo_time

#下一页按钮
def next_page_action(webdriver):
    webdriver.find_element_by_xpath(".//a[@class='page next S_txt1 S_line1']").click()
    webdriver.implicitly_wait(10)

#转发一条微博
def forword_weibo(webdriver, weibo, forword_comment):
    weibo.weibo_driver.find_element_by_xpath(".//span[@node-type='forward_btn_text']").click()
    time.sleep(2)
    forward_driver = webdriver.find_element_by_class_name('layer_forward')
    text_driver = forward_driver.find_element_by_tag_name('textarea')
    text_driver.clear()
    text_driver.send_keys(forword_comment.decode('utf-8'))
    forward_driver.find_element_by_class_name('W_btn_a').click()

if __name__ == '__main__':
    time_parse('05月20日 18:30')



