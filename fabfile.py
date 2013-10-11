# -*- coding: utf-8 -*- 

import yaml
from fabric.api import local,cd,run,env,put
from config import *

env.user = USER
env.hosts = HOSTS
env.password = PASSWORD


def native():
    with cd(LOCAL_DEPOT):
        local('tar czvf /tmp/this.tar.gz *')
    for host in HOSTS: 
        put('/tmp/this.tar.gz','/tmp/target.tar.gz')

def remote():
    print 'remote operate'
    with cd('/tmp'):
        run('tree')



def start():
    native()
