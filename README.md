###S3自动化工具！！

可实现批量操作S3等下载上传等操作，具备可拓展性，简单易懂！

## 环境依赖 
boto3 v1.24.68 

python版本: python >= 3.7

>boto3 是 python 中实现连接 S3 的库/软件包，可以拿来直接调用操作 S3（下载、上传等等）；
> 此外 boto3 只支持 python3.7 及以上版本，建议安装高一些的 python 版本。

## 部署步骤 

pip install boto3==1.24.68

>在设置里加这个库或者在py文件里安装都可以，boto3版本不一定非要1.24.68

## 目录结构
```
├─Base  #基础工具层-可拓展
│      basePath.py  #基础路径
│      baseS3Helper.py  #S3基础操作
│      utils.py  #额外方法
│          
├─DemandScript
│      bussinessS3.py  #S3的一层封装-简单操作
│      demandS3.py  #S3的定制需求-复杂操作
│      
├─FilesStation  #用于储存S3文件的目录
│─Config.ini  #S3配置信息
│─README.md
```
