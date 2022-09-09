# -*- codeing = utf-8 -*-
# @Time: 2022/9/8 19:44
# @Author: jiadong
# @File：utils.py
# @Software：PyCharm


import os
from configparser import RawConfigParser
from Base.basePath import BasePath

def read_config_ini(configpath):
    '''读取ini文件'''
    config = RawConfigParser() #内置读取config配置文件方法
    config.read(configpath,encoding='utf-8')
    return config






if __name__ == "__main__":
    pass