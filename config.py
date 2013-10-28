# -*- coding: utf-8 -*-
import os

USER = 'test'
HOSTS = ['127.0.0.1']
PASSWORD = '123456'


PROJECT_NAME = 'Fileserver' #项目名称
LOCAL_DEPOT = '/tmp/depot/' #临时项目仓库
LOCAL_DEPLOY = '/tmp/deploy/' 
GIT_DEOPT = 'https://github.com/neo1989/Fileserver.git'

REMOTE_DEPOT = '/var/www/' #生产环境根目录
REMOTE_BACKUP = '/data/webbackup/' #生产环境备份目录

RELOAD = ['touch /tmp/reload',] #重启相关服务
 

#EOF
#加载服务器配置
extend = os.path.join(os.path.abspath(os.path.dirname(__file__)),'conf_extend.py')
if os.path.exists(extend):
    from conf_extend import *
