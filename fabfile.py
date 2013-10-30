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

def collect_from_git():
    if os.path.exists(TMP_DEPOT):
        local('rm %s -rf' % TMP_DEPOT)
    local('mkdir -p %s' % TMP_DEPOT)

    os.chdir(TMP_DEPOT)
    local('git clone %s' % GIT_DEOPT)

    os.chdir(TMP_DEPOT+PROJECT_NAME)
    local('git checkout %s' % x['commit'])

    if os.path.exists(TMP_DEPLOY):
        local('rm %s -rf' % TMP_DEPLOY)
    local('mkdir -p %s' % TMP_DEPLOY)

    source = TMP_DEPOT + PROJECT_NAME +'/'
    dest = TMP_DEPLOY 

    for f in x['files']:
        if f.endswith('/'):
            f = f[:-1]
        m = re.split(r'/',f)
        _mkdir(m[:-1])
        local('cp -R %s %s' % (source+f,dest+f))

def collect_from_local():
    if os.path.exists(TMP_DEPLOY):
        local('rm %s -rf' % TMP_DEPLOY)
    local('mkdir -p %s' % TMP_DEPLOY)

    source = LOCAL_DEPOT
    dest = TMP_DEPLOY 

    for f in x['files']:
        if f.endswith('/'):
            f = f[:-1]
        m = re.split(r'/',f)
        _mkdir(m[:-1])
        local('cp -R %s %s' % (source+f,dest+f))


def _mkdir(data=[]):
    path = TMP_DEPLOY + '/'.join(data)
    if not os.path.exists(path):
        local('mkdir -p %s' % path)

def upload():
    with lcd(TMP_DEPLOY):
        local('tar czvf /tmp/target.tar.gz *'),
    put('/tmp/target.tar.gz','/tmp/target.tar.gz')

def remote():
    run('rm -rf /tmp/target/')
    run('mkdir /tmp/target/')
    run('tar xvf /tmp/target.tar.gz -C /tmp/target/')

    #备份生产环境代码
    t = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
    with cd(REMOTE_DEPOT):
        run('tar czvf %s%s_%s.tar.gz *' % (REMOTE_BACKUP,PROJECT_NAME,t))

    #更新代码
    run('cp /tmp/target/* %s -R' % REMOTE_DEPOT)

    #reload
    for r in RELOAD:
        run(r)

def g():
    collect_from_git()
    upload()
    remote()

def l():
    collect_from_local()
    upload()
    remote()
