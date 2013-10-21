# -*- coding: utf-8 -*- 

import yaml
import os
from fabric.api import local,lcd,cd,run,env,put
from config import *

env.user = USER
env.hosts = HOSTS
env.password = PASSWORD

yml = open('yml')
x = yaml.load(yml)

def before():
    if os.path.exists(LOCAL_DEPOT):
        local('rm %s -rf' % LOCAL_DEPOT)
    local('mkdir %s' % LOCAL_DEPOT)

    os.chdir(LOCAL_DEPOT)
    local('/usr/bin/git clone %s' % GIT_DEOPT)


def upload():
    print 'upload tar file'
    put('/tmp/this.tar.gz','/tmp/target.tar.gz')

def remote():
    print 'remote operation'
    with cd('/tmp'):
        run('tree')


def start():
    before()
