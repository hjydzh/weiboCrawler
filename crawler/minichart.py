#coding:utf-8
from Tkinter import *
import time


def send_msg():
    msgcontent = u'我:' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n '
    text_msglist.insert('0.0', text_msg.get('0.0', END))
    text_msglist.insert('0.0', msgcontent, 'green')


if __name__ == '__main__':
    root = Tk()
    root.title(u'与她聊天中')
    frame_left_top   = Frame(width=380, height=270, bg='blue')
    frame_left_center  = Frame(width=380, height=100, bg='blue')
    frame_left_bottom  = Frame(width=380, height=20)
    frame_right     = Frame(width=170, height=400, bg='white')
    text_msglist    = Text(frame_left_top)
    text_msg      = Text(frame_left_center)
    button_sendmsg   = Button(frame_left_bottom, text=u'发送', command=send_msg)
    text_msglist.tag_config('green', foreground='#008B00')
    frame_left_top.grid(row=0, column=0, padx=2, pady=5)
    frame_left_center.grid(row=1, column=0, padx=2, pady=5)
    frame_left_bottom.grid(row=2, column=0)
    frame_right.grid(row=0, column=1, rowspan=3, padx=4, pady=5)
    frame_left_top.grid_propagate(0)
    frame_left_center.grid_propagate(0)
    frame_left_bottom.grid_propagate(0)
    #把元素填充进frame
    text_msglist.grid()
    text_msg.grid()
    button_sendmsg.grid(sticky=E)
    #主事件循环
    root.mainloop()
