# -*- coding: utf-8 -*-
import os

USER = 'test'
HOSTS = ['127.0.0.1']
PASSWORD = '123456'

YML = 'yml'     #默认的yml配置的filename 



#EOF
#加载服务器配置
extend = os.path.join(os.path.abspath(os.path.dirname(__file__)),'conf_extend.py')
if os.path.exists(extend):
    from conf_extend import *
