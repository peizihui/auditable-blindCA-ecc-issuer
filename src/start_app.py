#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
#author:rujia
#website:www.rujia.uk
#version:1.0
from demo import *
from flask import Flask
from config import conf



if __name__ == "__main__": 
    app.run(host=conf.HOST,port=conf.PORT,debug=True)