#-*- coding:utf-8 -*-

import os
import json
import time
import sqlite3

def read_config():
    configFile = 'WebHook.config'
    if not os.path.exists(configFile):
        print('Config File is not exist!')
        return False
    else:
        fp = open(configFile, 'r')
        config=json.load(fp)
        fp.close()
        return config

def clone(address):
    clone_address = 'git clone ' + address + ' webfiles'
    os.system(clone_address)

def pull():
    os.system('cd webfiles && git pull')

def check(useragent):
    useragent = useragent[:13]
    if useragent == 'GitHub-Hooksh':
        return True
    else:
        return False

def deploy():
    if read_config():
        address = read_config()['Address']
        if os.path.exists('webfiles'):
            print('Pulling from GitHub...\n')
            pull()
            print('Done!\n')
            return gettimenow()+'  Pulled successfully!'
        else:
            print('Cloning form GitHub...\n')
            clone(address)
            print('Done!\n')
            return gettimenow()+'  Cloned successfully!'
    else:
        return False

def gettimenow():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
