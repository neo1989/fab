# -*- coding: utf-8 -*- 

import yaml
import os
import re
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
    local('mkdir -p %s' % LOCAL_DEPOT)

    os.chdir(LOCAL_DEPOT)
    local('/usr/bin/git clone %s' % GIT_DEOPT)

    os.chdir(LOCAL_DEPOT+PROJECT_NAME)
    local('/usr/bin/git checkout %s' % x['commit'])

    if os.path.exists(LOCAL_DEPLOY):
        local('rm %s -rf' % LOCAL_DEPLOY)
    local('mkdir -p %s' % LOCAL_DEPLOY)

    source = LOCAL_DEPOT + PROJECT_NAME +'/'
    dest = LOCAL_DEPLOY 

    for f in x['files']:
        if f.endswith('/'):
            f = f[:-1]
        m = re.split(r'/',f)
        _mkdir(m[:-1])
        local('cp -R %s %s' % (source+f,dest+f))

def _mkdir(data=[]):
    path = LOCAL_DEPLOY + '/'.join(data)
    if not os.path.exists(path):
        local('mkdir -p %s' % path)

def upload():
    print 'upload tar file'
    put('/tmp/this.tar.gz','/tmp/target.tar.gz')

def remote():
    print 'remote operation'
    with cd('/tmp'):
        run('tree')


def start():
    before()
