# -*- coding: utf-8 -*- 

from fabric.api import local,cd,run,env
from config import *

env.hosts = HOSTS
env.password = PASSWORD

def remote():
    print 'remote operate'
    run('ifconfig')


