# -*- coding: utf-8 -*- 

import yaml
import os
import re
import time
from fabric.api import local,lcd,cd,run,env,put,sudo,settings
from config import *

env.user = USER
env.hosts = HOSTS
env.password = PASSWORD

yml = open('yml')
x = yaml.load(yml)

def collect():
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
    with lcd(LOCAL_DEPLOY):
        local('tar czvf /tmp/target.tar.gz *'),
    put('/tmp/target.tar.gz','/tmp/target.tar.gz')

def remote():
    run('rm -rf /tmp/target/')
    run('mkdir /tmp/target/')
    run('tar xvf /tmp/target.tar.gz -C /tmp/target/')

    #备份生产环境代码
    t = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
    with cd(REMOTE_DEPOT):
        run('tar czvf %s%s.tar.gz *' % (REMOTE_BACKUP,t))

    #更新代码
    run('cp /tmp/target/* %s -R' % REMOTE_DEPOT)

    #reload
    for r in RELOAD:
        run(r)


def start():
    collect()
    upload()
    remote()
