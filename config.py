# -*- coding: utf-8 -*-
import os

HOSTS = ['test@127.0.0.1']
PASSWORD = '123456'


PROJECT = 'test'


#EOF
#加载服务器配置
extend = os.path.join(os.path.abspath(os.path.dirname(__file__)),'conf_extend.py')
if os.path.exists(extend):
    from conf_extend import *
