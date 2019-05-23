#!/usr/bin/python
# -*- coding: utf-8 -*-

# author:rujia
# website:www.rujia.uk
# version:1.0

from flask import request, session, json, render_template
from . import app
from core import blind_demo
from core import until

@app.route('/')
def default():
    return render_template('/index.html')


@app.route('/index')
def index():
    return render_template('/index.html')


@app.route('/index_register')
def index_register():
    return render_template('/index_register.html')


@app.route('/tracing')
def tracing():
    return render_template('tracing.html')


@app.route('/init', methods=['GET'])
def init():
    try:
        uid = until.get_mac_address()
        
        p = session.get(uid+'p')
        a = session.get(uid+'a')
        b = session.get(uid+'b')
        n = session.get(uid+'n')
        
        secp = session.get(uid+'secp')
        
        if secp == 'secp256k1':
            params = blind_demo.choose_parameters_secp256k1()
        elif secp == 'secp192k1':
            params = blind_demo.choose_parameters_secp192k1()
        
        orig_h = until.getObjFromSession(uid+'h_bytes',params.group)
        orig_g = until.getObjFromSession(uid+'g_bytes',params.group)
        
        
        orig_x = until.getObjFromSession(uid+'x_bytes',params.group)
        orig_y = until.getObjFromSession(uid+'y_bytes',params.group)
        orig_z = until.getObjFromSession(uid+'z_bytes',params.group)
        orig_gamma = until.getObjFromSession(uid+'gamma_bytes',params.group)
        orig_xi = until.getObjFromSession(uid+'xi_bytes',params.group)

        rjson = str(p) + '#' + str(a) + '#' + str(b) + '#' + str(n) + '#' + str(orig_g) + '#' + str(orig_h) \
        + '#' + str(secp) + "#" + str(orig_x) + '#' + str(orig_y) + '#' + str(orig_z) + '#' + str(orig_gamma) + '#' + str(orig_xi)

        return rjson
    except Exception:
        return '0'


@app.route('/setup', methods=['POST'])
def setup():
    try:
        uid = until.get_mac_address()

        secp = str(request.form['secp'])

        (
            p,
            a,
            b,
            n,
            g,
            h
            ) = (
            0,
            0,
            0,
            0,
            None,
            None
            )

        if secp == 'secp256k1':
            params = blind_demo.choose_parameters_secp256k1()
            p = 115792089237316195423570985008687907853269984665640564039457584007908834671663
            a = 0
            b = 7
            n = 115792089237316195423570985008687907852837564279074904382605163141518161494337
            g = params.g
            h = params.h

        elif secp == 'secp192k1':

            params = blind_demo.choose_parameters_secp192k1()
            p = 6277101735386680763835789423207666416102355444459739541047
            a = 0
            b = 3
            n = 6277101735386680763835789423061264271957123915200845512077
            g = params.g
            h = params.h
            
        until.putBytesToSession(uid+'g_bytes', g, params.group)
        until.putBytesToSession(uid+'h_bytes', h, params.group)
        
        session[uid+'p'] = p
        session[uid+'a'] = a
        session[uid+'b'] = b
        session[uid+'n'] = n
        
        session[uid+'secp'] = secp
        print(session.get(uid+'secp'))

        rjson = str(p) + '#' + str(a) + '#' + str(b) + '#' + str(n) + '#' + str(g) + '#' + str(h)
        return rjson
    except Exception:
        return '0'


# def getX(parax):
# ....parax = str(parax)
# ....parax = parax.split(',')[0]
# ....parax = parax[1:len(parax)]
# ....return parax

# def getY(paray):
# ....paray = str(paray)
# ....paray = paray.split(',')[1]
# ....paray = paray[1:len(paray)-1]
# ....return paray

@app.route('/issuerkey', methods=['POST'])
def issuerkey():
    try:
        uid = until.get_mac_address()
        secp = session.get(uid+'secp')
        print(session.get(uid+'secp'))
        
        if secp == 'secp256k1':
            params = blind_demo.choose_parameters_secp256k1()
        elif secp == 'secp192k1':
            params = blind_demo.choose_parameters_secp192k1()
        
        orig_h = until.getObjFromSession(uid+'h_bytes',params.group)
        orig_g = until.getObjFromSession(uid+'g_bytes',params.group)
        issuerparams = blind_demo.issuer_choose_keypair(params.group,orig_g)
        x = issuerparams.x
        y = issuerparams.y
        
        until.putBytesToSession(uid+'x_bytes', x, params.group)
        until.putBytesToSession(uid+'y_bytes', y, params.group)

        print(y)
        
        z = blind_demo.gnerate_common_z(params.group, orig_g, orig_h, y)
        until.putBytesToSession(uid+'z_bytes',z, params.group)
        
        rjson = str(x) + "#" + str(y) + "#" + str(z)
        return rjson
    except Exception:
        return '0' 


@app.route('/userkey', methods=['POST'])
def userkey():
    try:
        uid = until.get_mac_address()
        secp = session.get(uid+'secp')
        print(session.get(uid+'secp'))
        print(secp)

        if secp == 'secp256k1':
            params = blind_demo.choose_parameters_secp256k1()
        elif secp == 'secp192k1':
            params = blind_demo.choose_parameters_secp192k1()

        orig_g = until.getObjFromSession(uid+'g_bytes',params.group)

        userparams = blind_demo.user_choose_keypair(params.group,orig_g)

        xi = userparams.xi
        gamma = userparams.gamma
        
        until.putBytesToSession(uid+'gamma_bytes',gamma, params.group)
        until.putBytesToSession(uid+'xi_bytes',xi, params.group)

        rjson = str(gamma) + '#' + str(xi)
        
        print(rjson)

        return rjson
    except Exception:
        return '0'
