#author:rujia
#website:www.rujia.uk
#version:1.0

from flask import session,request,render_template
from . import app
from core import blind_demo

@app.route('/issuing')
def issuing():
    yt = str(request.args.get('pk'))
    contractAddress = str(request.args.get('contractAddress'))
    session['yt'] = yt
    session['cas'] = contractAddress
    print(contractAddress)
    return render_template('issuing.html')

@app.route("/initgamma", methods=['GET'])
def initgamma():
    try:
            #xi = session.get('xi')
            #gamma = session.get('gamma')
            
            # protocol one
            z = session.get('z')
            user = getUserObj()
            zu, xi = user.protocol_one()
            session['zu'] = zu
            y = session.get('y')
            rjson1 = str(user.UserKeypair.gamma) + ',' + str(xi) + ',' + str(z) + ',' + str(zu) + ',' + str(y)
            
            # protocol two
            upsilon = session.get('upsilon')
            mu = session.get('mu')
            d = session.get('d')
            s1 = session.get('s1')
            s2 = session.get('s2')
            z1 = session.get('z1')
            z2 = session.get('z2')
            a = session.get('a')
            b1 = session.get('b1')
            b2 = session.get('b2')
            
            rjson2 = str(upsilon) + ',' + str(mu) + ',' + str(d) + ',' + str(s1) + ',' + str(s2) + ',' + str(z1) + ',' + str(z2) + ',' + str(a)+ ',' + str(b1)+ ',' + str(b2)
            
            # protocol three
            t1 = session.get('t1')
            t2 = session.get('t2')
            t3 = session.get('t3')
            t4 = session.get('t4')
            t5 = session.get('t5')
            
            zeta1 = session.get('zeta1')
            zeta2 = session.get('zeta2')
            alpha = session.get('alpha')
            beta1 = session.get('beta1')
            beta2 = session.get('beta2')
            epsilon = session.get('epsilon')
            e = session.get('e')
            
            rjson3 = str(t1) + ',' + str(t2) + ',' + str(t3) + ',' + str(t4) + ',' + str(t5) + ',' + str(zeta1) + ',' + str(zeta2) + ',' + str(alpha)+ ',' + str(b1)+ ',' + str(beta1)+ ',' + str(beta2)+ ',' + str(epsilon)+ ',' + str(e)

            
            # protocol four
            c = session.get('c')
            r = session.get('r')
            
            rjson4 = str(c) + ',' + str(r)
            # protocol five
            
            rho = session.get('rho')
            omega = session.get('omega')
            sigma1 = session.get('sigma1')
            sigma2 = session.get('sigma2')
            delta = session.get('delta')
            
            rjson5 = str(rho) + ',' + str(omega) + ',' + str(sigma1) + ',' + str(sigma2) + ',' + str(delta)
            
           
            m = session.get('m')
            if(m != None):
                m = m.decode('utf-8')
            else:
                m = 'None'
            
            rjson = rjson1 + ',' + rjson2 + ',' + rjson3 + ',' + rjson4 + ',' + rjson5 + ',' + m
            
            contractAddress = session.get('cas')
            xiupsilon = session.get('xiupsilon')
            
            rjson = rjson + ',' + str(contractAddress) + ',' + str(xiupsilon)
            
            return rjson
    except Exception:
        return "0"
    

@app.route("/issuerExecuteTwo", methods=['GET'])
def issuerExecuteTwo():
    try:
            zu = int(session.get('zu')) # assuming get from the user
            
            issuer = getIssuerObj()
            issuer.protocol_two(zu)
            
            session['z1'] = issuer.z1
            session['z2'] = issuer.z2
            session['a'] = issuer.a
            session['b1'] = issuer.b1
            session['b2'] = issuer.b2
            session['d'] = issuer.d
            session['mu'] = issuer.mu
            session['s1'] = issuer.s1
            session['s2'] = issuer.s2
            
            rjson = str(issuer.upsilon) + ',' + str(issuer.mu) + ',' + str(issuer.s1) + ',' + str(issuer.s2) + ',' + str(issuer.d) + ',' + str(issuer.z1) + ',' + str(issuer.z2) + ',' + str(issuer.a) + ',' + str(issuer.b1)+ ',' + str(issuer.b2)
            
            return rjson
    except Exception as e:
        print(e)
        return "0"


@app.route("/userExecuteThree", methods=['POST'])
def userExecuteThree():
    try:
            user = getUserObj()
           
            z1 = int(session.get('z1'))
            a = int(session.get('a'))
            b1 = int(session.get('b1'))
            b2 = int(session.get('b2'))
            
            
            m = str(request.form['m'])
            
            print(m)
            
            m = bytes(m,'utf-8')
            session['m'] = m
            
            user.protocol_three(z1, a, b1, b2, m)
            
            session['zeta1'] = user.zeta1
            session['zeta2'] = user.zeta2
            session['alpha'] = user.alpha
            session['alpha'] = user.alpha
            session['beta1'] = user.beta1
            session['beta2'] = user.beta2
            session['epsilon'] = user.epsilon
            session['e'] = user.e
            
            rjson = str(user.zeta1) + ',' + str(user.zeta2) + ',' + str(user.t1) + ',' + str(user.t2) + ',' + str(user.t3) + ',' + str(user.t4) + ',' + str(user.t5) + ',' + str(user.alpha)+ ',' + str(user.beta1)+ ',' + str(user.beta2)+ ',' + str(user.epsilon)+ ',' + str(user.e)
            
            return rjson
    except Exception as e1:
        print(e1)
        return "0"


@app.route("/issuerExecuteFour", methods=['GET'])
def issuerExecuteFour():
    try:
            issuer = getIssuerObj()
            
            e = int(session.get('e'))
            r,c,_,_,_  = issuer.protocol_four(e)
            
            session['r'] = r
            session['c'] = c
            
            rjson = str(r) + ',' + str(c)
            return rjson
    except Exception as e:
        print(e)
        return "0"    

@app.route("/issuerExecuteSix", methods=['GET'])
def issuerExecuteSix():
    try:
            issuer = getIssuerObj()
            
            print(session.get('xi'))
            
            xi = int(session.get('xi'))
            
            contractAddress = session.get('cas')
            
            xiupsilon = issuer.protocol_six(xi) 
            session['xiupsilon'] = xiupsilon
            
            rjson  = str(xi) + "," + str(xiupsilon) + "," + str(contractAddress)
            return rjson
        
    except Exception as e:
        print(e)
        return "0" 
  
@app.route("/userExecuteFive", methods=['GET'])
def userExecuteFive():
    try:
            user = getUserObj()
           
            r = session.get('r')
            c = session.get('c')
            s1 = session.get('s1')
            s2 = session.get('s2')
            d = session.get('d')
            
            rho, omega, sigma1, sigma2, delta = user.protocol_five(r, c, s1,s2, d)
            
            session['rho'] = rho
            session['omega'] = omega
            session['sigma1'] = sigma1
            session['sigma2'] = sigma2
            session['delta'] = delta
            
            rjson = str(rho) + ',' + str(omega) + ',' + str(sigma1) + ',' + str(sigma2) + ',' + str(delta)
            
            return rjson
    except Exception as e1:
        print(e1)
        return "0"

def getIssuerObj():
    try:
            L = session.get('L')
            N = session.get('N')
            p = session.get('p')
            q = session.get('q')
            g = session.get('g')
            h = session.get('h')
           
            params = blind_demo.Parameters(L, N, p, q, g, h)
            
            x = session.get('x')
            y = session.get('y')
            yt = int(session.get('yt'))
            z = session.get('z')
            
            
            upsilon = session.get('upsilon')
            mu = session.get('mu')
            d = session.get('d')
            s1 = session.get('s1')
            s2 = session.get('s2')
            
            #upsilon = 1131744774912427240787421411389040568170382216
            #mu = 323113775694352543177133061757687809309917194147
            #s1 = 80265387361124049999679494046599184323218995737
            #s2 = 363145392284651453379471000225041771070074440315
            #d = 276662341117674262269660624603213684542129423868
            
            issuer = blind_demo.Issuer(L,N,p,q,g,h,x,y,params)
            issuer.start(z,upsilon,mu,d,s1,s2, yt)
            
            return issuer
    except Exception:
        return None
    
    
def getUserObj():
    try:
            L = session.get('L')
            N = session.get('N')
            p = session.get('p')
            q = session.get('q')
            g = session.get('g')
            h = session.get('h')
            z = session.get('z')
            
            params = blind_demo.Parameters(L, N, p, q, g, h)
            
            xi = session.get('xi')
            gamma = session.get('gamma')
            
            t1 = session.get('t1')
            t2 = session.get('t2')
            t3 = session.get('t3')
            t4 = session.get('t4')
            t5 = session.get('t5')
            
            y = session.get('y')
            
            user = blind_demo.User(L,N,p,q,g,h,gamma,xi,params)
            user.start( t1, t2, t3, t4, t5, z, y)
            
            return user
    except Exception:
        return None
    