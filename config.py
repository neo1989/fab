# -*- coding: utf-8 -*-
import os

USER = 'test'
HOSTS = ['127.0.0.1']
PASSWORD = '123456'

YML = 'yml' #yml配置的filename

PROJECT_NAME = 'Fileserver' #项目名称
TMP_DEPOT = '/tmp/depot/'   #临时项目仓库
TMP_DEPLOY = '/tmp/deploy/' #发布区 
GIT_DEOPT = 'https://github.com/neo1989/Fileserver.git'


LOCAL_DEPOT = '/var/www/fileserver/' #本地开发环境根目录
REMOTE_DEPOT = '/var/www/fileserver/' #生产环境根目录
REMOTE_BACKUP = '/data/webbackup/' #生产环境备份目录

RELOAD = ['touch /tmp/reload',] #重启相关服务
 

#EOF
#加载服务器配置
extend = os.path.join(os.path.abspath(os.path.dirname(__file__)),'conf_extend.py')
if os.path.exists(extend):
    from conf_extend import *
