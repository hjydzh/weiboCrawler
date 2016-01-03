#coding:utf-8
from __future__ import division

#根据粉丝数量，微博转发、评论、赞，这几个参数评估微博受欢迎质量,返回选中微博index和该微博中选中的评论
def nums_strategy(weibos):
    for weibo in weibos:
        if weibo is None:
            continue
        author_info = weibo.author_info
        if weibo.comment_list is None or weibo.author_name != author_info.name:
            print  weibo.author_name, author_info.name
            weibo.mark = 0.0
            continue
        print '%s, 关注:%s ,粉丝:%s, 微博:%s -----转发:%s(%s), 评论:%s(%s),, 赞:%s(%s)' % (weibo.author_name,author_info.focus_num, author_info.fans_num, author_info.weibo_num, weibo.forward_num,weibo.forward_num/author_info.fans_num, weibo.comment_num,weibo.comment_num/author_info.fans_num,weibo.good_num,weibo.good_num/author_info.fans_num)
        weibo.mark = 10000*(0.3*weibo.forward_num/author_info.fans_num+0.5*weibo.comment_num/author_info.fans_num+0.2*weibo.good_num/author_info.fans_num)
        selected_comment = __second_popular_comment(weibo.comment_list)
        if selected_comment is None:
            continue
        weibo.selected_comment = selected_comment
        print('选中评论为:' + selected_comment.comment)
    return sorted(weibos, key=lambda w: w.mark,reverse=True)



#返回第二受欢迎的评论
def __second_popular_comment(comments):
    comments = filter(lambda c: c.comment != '', comments)
    if not any(comments):
        return None
    if len(comments) == 1:
        return comments[0]
    return sorted(comments, key=lambda comment: comment.good_nums)[-1]

