#coding:utf-8
from commons.CommonConst import *

def get_passwd_dict():
    dict = {}
    with open(Const.PASSWD_FILE) as file:
        for line in file:
            split_line = line.strip().split('=')
            dict[split_line[0]] = split_line[1]
    return dict
