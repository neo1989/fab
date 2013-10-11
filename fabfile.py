# -*- coding: utf-8 -*- 

import yaml
from fabric.api import local,cd,run,env
from config import *

env.hosts = HOSTS
env.password = PASSWORD


def native():
    with cd(Local_depot):
        local('tar czvf /tmp/this.tar.gz *')
    local('cd /tmp/ && scp this.tar.gz %s:/tmp/remote/' % HOSTS)

def remote():
    print 'remote operate'
    with cd('/tmp'):
        run('tree')



def start():
    native()

