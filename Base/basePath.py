# -*- codeing = utf-8 -*-
# @Time: 2022/9/8 19:45
# @Author: xiaowo
# @File：basePath.py
# @Software：PyCharm

import os

class BasePath(object):

    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 根目录
    CONFIG_FILE = os.path.join(PROJECT_ROOT, "Config.ini") #配置文件目录
    FILE_STATION = os.path.join(PROJECT_ROOT, "FilesStation/") #文件工作站-用于处理文件数据
