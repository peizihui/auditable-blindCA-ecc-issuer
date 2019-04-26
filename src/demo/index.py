

#author:rujia
#website:www.rujia.uk
#version:1.0

from flask import request,session,json,render_template
from . import app
#from . import db
from core import blind_demo



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

@app.route("/init", methods=['GET'])
def init():
	try:
			#L = session.get('L')
			#N = session.get('N')
			p = session.get('p')
			q = session.get('q')
			g = session.get('g')
			
			x = session.get('x')
			y = session.get('y')
			h = session.get('h')
			z = session.get('z')
			
			xi = session.get('xi')
			gamma = session.get('gamma')
			
			rjson = str(p) + ',' + str(q) + ',' + str(g) + ',' + str(x) + ',' + str(y) + ',' + str(h) + ',' + str(z) + ',' + str(xi) + ',' + str(gamma) 
			
			return rjson
	except Exception:
		return "0"

@app.route("/setup", methods=['POST'])
def setup():
	try:
			session.clear()
			
			L = int(request.form['L'])
			N = int(request.form['N'])
			params = blind_demo.choose_parameters(L,N)
			
			session['L'] = L
			session['N'] = N
			session['p'] = params.p
			session['q'] = params.q
			session['g'] = params.g
			session['h'] = params.h
			
			rjson = json.dumps(params)
			
			return rjson
	except Exception:
		return "0"

@app.route("/issuerkey", methods=['POST'])
def issuerkey():
	try:
			L = session.get('L')
			N = session.get('N')
			p = session.get('p')
			q = session.get('q')
			g = session.get('g')
			h = session.get('h')
			
			params = blind_demo.Parameters(L, N, p, q, g, h)
			
			issuerparams = blind_demo.issuer_choose_keypair(params)
			
			x = issuerparams.x
			y = issuerparams.y
			session['x'] = x
			session['y'] = y
			
			z = blind_demo.gnerate_common_z(params, h, y)
			session['z'] = z
			
			#tracerparams = blind_demo.tracer_choose_keypair(params)
			#xt = tracerparams.xt
			#yt = tracerparams.yt
			
			
			## set the tracer's private key and public key
			#session['xt'] = xt
			#session['yt'] = yt

			#upsilon = 1131744774912427240787421411389040568170382216
			#mu = 323113775694352543177133061757687809309917194147
			#s1 = 80265387361124049999679494046599184323218995737
			#s2 = 363145392284651453379471000225041771070074440315
			#d = 276662341117674262269660624603213684542129423868
			
			session['upsilon'] = blind_demo.rand_less_than(params.q, params.N)
			session['mu'] = blind_demo.rand_less_than(params.q, params.N)
			session['d'] = blind_demo.rand_less_than(params.q, params.N)
			session['s1'] = blind_demo.rand_less_than(params.q, params.N)
			session['s2'] = blind_demo.rand_less_than(params.q, params.N)
			
			rjson = str(x) + ',' + str(y)  + ',' + str(z)
			
			return rjson
	except Exception:
		return "0"

@app.route("/userkey", methods=['POST'])
def userkey():
	try:
			L = session.get('L')
			N = session.get('N')
			p = session.get('p')
			q = session.get('q')
			g = session.get('g')
			h = session.get('h')
			params = blind_demo.Parameters(L, N, p, q, g, h)
			
			issuerparams = blind_demo.user_choose_keypair(params)
			session['xi'] = issuerparams.xi
			session['gamma'] = issuerparams.gamma
			
			t1 = blind_demo.rand_less_than(params.q, params.N)
			t2 = blind_demo.rand_less_than(params.q, params.N)
			t3 = blind_demo.rand_less_than(params.q, params.N)
			t4 = blind_demo.rand_less_than(params.q, params.N)
			t5 = blind_demo.rand_less_than(params.q, params.N)
			
			#t1 = 53469262023230480563475615733216614368413001046
			#t2 = 108250248297254881989205148547347791955729098453
			#t3 = 378917074496268035816520047086947221659871012331
			#t4 = 133459743642956919437859148575716353228269709357
			#t5 = 7272773057241985420455995988200180650086327435
			
			session['t1'] = t1
			session['t2'] = t2
			session['t3'] = t3
			session['t4'] = t4
			session['t5'] = t5
			
			rjson = json.dumps(issuerparams)
			
			return rjson
	except Exception:
		return "0"