#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:rujia
#website:www.rujia.uk
#version:1.0

from demo import *
from config import conf
from flask import Flask, session 
from flask_session import Session, FileSystemSessionInterface
#import os


if __name__ == "__main__":
    print ("""
      
  |     |    _______    |
  |     |   |       |   |_______
  |     |   |       |   |      |
  |_____|   |_______|   |______|  v0.0.1
           
""")

#app.config['SESSION_TYPE'] = 'filesystem'
#app.config["SECRET_KEY"] = "rujia"  # set random key 
#app.config['SESSION_FILE_DIR'] = './my_sessions' 
#app.config['SESSION_PERMANENT'] = True
#app.config['PERMANENT_SESSION_LIFETIME'] = 3000   #timout in seconds 

#create and configure flask-session  
#sess = Session()  

#bind app to flask-session  
#sess.init_app(app) 

app.run(host=conf.HOST,port=conf.PORT,debug=True)
#remove debug=True for production