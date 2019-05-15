#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
#author:rujia
#website:www.rujia.uk
#version:1.0

from demo import *
from config import conf
from flask import Flask, session
#import os

if __name__ == "__main__":
    app.run(host=conf.HOST,port=conf.PORT,debug=True)
