# -*- codeing = utf-8 -*-
# @Time: 2022/9/8 21:59
# @Author: xiaowo
# @File：demandS3.py
# @Software：PyCharm
import time

from DemandScript.bussinessS3 import BusinessS3


class DemandS3(object):

    def __init__(self):
        self.s3 = BusinessS3()

    """
    Excel文件自动生成ack后缀文件
    :param download_path: 下载文件的目录路径(注：该目录下即是文件)
    :param upload_path: 上传文件至S3的目录路径(注：该目录下即是文件)
    :return: 打印输出
    """
    def auto_to_ack(self,download_path):
        self.s3.download_file_to_FileStation(download_path)
        self.s3.add_prefix_suffix(".ack1")
        self.s3.upload_file_to_s3("")




if __name__ == '__main__':
    demandS3 = DemandS3()
    demandS3.auto_to_ack('')

