# -*- coding: utf-8 -*- 

import yaml
from fabric.api import local,cd,run,env
from config import *

env.hosts = HOSTS
env.password = PASSWORD


def native():
    with cd(LOCAL_DEPOT):
        local('tar czvf /tmp/this.tar.gz *')
    for host in HOSTS: 
        local('scp /tmp/this.tar.gz  %s:/tmp/' % host)

def remote():
    print 'remote operate'
    with cd('/tmp'):
        run('tree')



def start():
    native()

