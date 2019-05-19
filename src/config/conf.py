# coding: utf-8

import os

# python -m pip install pickle
# WEBSITE CONFIG #
HOST = '0.0.0.0'
PORT = 8081
#curpath = os.path.dirname(__file__)
#curpath = curpath[0:int(curpath.index('\config'))]

# APPLICATION CONFIG #
SETTINGS = {
    #'template_path': curpath + '\\templates',
    #'static_path': curpath + '\\static',
    'template_path': '../templates',
    'static_path': '../static',
    'cookie_secret': '!@#$%^&*()_+',
    'xsrf_cookies': True,
    'debug': False,
    'access_log': True
}

# DATABASE CONFIG #
#DATABASE_DRIVER = 'mongo'
#DATABASE_HOST_PORT = ''
#DATABASE_USER = 'multi_sig'
#DATABASE_PASS = 'multi_sig'
#DATABASE_DB = 'app_db'
#DATABASE_CONDITION = 'ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'
