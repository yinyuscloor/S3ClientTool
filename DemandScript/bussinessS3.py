# -*- codeing = utf-8 -*-
# @Time: 2022/9/8 20:22
# @Author: jiadong
# @File：bussinessS3.py
# @Software：PyCharm
import os
from Base.baseS3Helper import S3Helper
from Base.basePath import BasePath

class BusinessS3(object):

    def __init__(self):
        self.S3 = S3Helper()
        self.bucket_name = 'bucket_name' #桶名称，自定义！！
        self.dicpath = BasePath.FILE_STATION #FileStation目录路径

    """
    下载目录下的所有文件至FileStation文件夹
    :param download_dicpath: 下载文件的目录路径(注：该目录下即是文件)
    :return: 打印输出
    """
    def download_file_to_FileStation(self,download_dicpath):
        filelist = self.S3.get_list_s3(self.bucket_name,download_dicpath)
        for file in filelist:
            self.S3.download_file_s3(self.bucket_name , download_dicpath + file , self.dicpath)
            print("下载【{}】目录下的【{}】成功".format(download_dicpath,file))


    """
    给FileStation文件夹下的文件加前缀和后缀——此方法尽量不要动，不适合单独使用！！
    :param suffix: 修改文件的后缀名，如 ack1
    :return: 打印输出
    """
    def add_suffix(self,suffix):
        filelist = os.listdir(self.dicpath) #获取指定目录下的所有子目录和文件名
        if len(filelist) >= 1:
            for filename in filelist:
                oldname = self.dicpath + os.sep + filename  # os.sep添加系统分隔符, 设置旧文件名（就是路径+文件名）
                newname = self.dicpath + os.sep + filename + suffix # 设置新文件名
                os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
                print("修改FilesStation下的【{}】名称成功".format(filename))
        else:
            return "当前FilesStation目录下无文件！！"

    """
    修改FileStation文件夹下的后缀
    :param before: 修改之前的后缀名，
    :param next: 修改之后的后缀名，
    :return: 打印输出
    """
    def ammend_suffix(self,before,next):
        filelist = os.listdir(self.dicpath) #获取指定目录下的所有子目录和文件名
        if len(filelist) >= 1:
            for filename in filelist:
                oldname = self.dicpath + os.sep + filename  # os.sep添加系统分隔符, 设置旧文件名（就是路径+文件名）
                newname = oldname.replace(before, next)
                os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
                print("修改FilesStation下的【{}】名称成功,由{}变更为{}".format(filename,before,next))
        else:
            return "当前FilesStation目录下无文件！！"



    """
    删除FileStation文件夹下的所有文件，必要操作
    :return: 打印输出
    """
    def delete_all_FileStation(self):
        filelist = os.listdir(self.dicpath)
        for file in filelist:
            os.remove(self.dicpath + file) # 该命令删除文件
            print("【{}】文件已删除".format(file))

    """
    上传FileStation文件夹下的所有文件至S3
    :param s3_dir: 要上传到的s3文件夹名称
    :return: 打印输出
    """
    def upload_file_to_s3(self,s3_dir=None):
        filelist = os.listdir(self.dicpath)
        if len(filelist) >= 1:
            for file in filelist:
                self.S3.upload_file_s3(self.dicpath + os.sep + file,self.bucket_name,s3_dir)
                print("上传本地【{}】目录下的【{}】至S3成功".format(self.dicpath,file))
        else:
            return "当前FilesStation目录下无文件！！"






if __name__ == '__main__':
    BusinessS3 = BusinessS3()
    # BusinessS3.download_file_to_FileStation('')
    # BusinessS3.add_prefix_suffix(".ack1")
    BusinessS3.delete_all_FileStation()
    # BusinessS3.ammend_suffix(".ack1",".ack2")
    # BusinessS3.upload_file_to_s3("")