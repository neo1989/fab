# -*- coding: utf-8 -*-
import os

USER = 'test'
HOSTS = ['127.0.0.1']
PASSWORD = '123456'


LOCAL_DEPOT = '/tmp/depot/' #临时项目仓库
PROJECT_NAME = 'fab' #项目名称
GIT_DEOPT = 'https://github.com/neo1989/fab.git'


#EOF
#加载服务器配置
extend = os.path.join(os.path.abspath(os.path.dirname(__file__)),'conf_extend.py')
if os.path.exists(extend):
    from conf_extend import *
