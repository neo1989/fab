# -*- coding: utf-8 -*- 

import yaml
import os
import sys 
import re
import time
from fabric.api import local,lcd,cd,run,env,put,sudo,settings
from config import *

env.user = USER
env.hosts = HOSTS
env.password = PASSWORD

def loadConfig(func):
    def inner(*args,**kwargs):
        global x,PROJECT_NAME,TMP_DEPOT,TMP_DEPLOY,GIT_DEOPT,LOCAL_DEPOT,REMOTE_DEPOT,REMOTE_BACKUP,RELOAD
        try:
            ymlfile = kwargs['yml'] 
        except Exception, e:
            ymlfile = YML

        ymlDetail = open(ymlfile)
        x = yaml.load(ymlDetail)

        PROJECT_NAME = x['PROJECT_NAME']            #项目名称
        TMP_DEPOT = x['TMP_DEPOT']                  #临时项目仓库
        TMP_DEPLOY = x['TMP_DEPLOY']                #发布区 
        GIT_DEOPT = x['GIT_DEOPT']                  #远程GIT仓库 


        LOCAL_DEPOT = x['LOCAL_DEPOT']              #本地开发环境根目录
        REMOTE_DEPOT = x['REMOTE_DEPOT']            #生产环境根目录
        REMOTE_BACKUP = x['REMOTE_BACKUP']          #生产环境备份目录

        RELOAD = x['RELOAD']                        #重启相关服务

        return func(*args,**kwargs)
    return inner
 

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
    if RELOAD:
        map(lambda r: sudo(r), filter(lambda x: x,RELOAD))

@loadConfig
def g(yml):
    collect_from_git()
    upload()
    remote()

@loadConfig
def l(yml):
    collect_from_local()
    upload()
    remote()



