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
            
            # protocol one
            user = getUserObj()
            orig_gamma = blind_demo.getObjFromSession('gamma_bytes',user.parameters.group)
            orig_z = blind_demo.getObjFromSession('z_bytes',user.parameters.group)
            
            zu, xi = user.protocol_one()
            
            session['zu'] = str(zu)
            print(zu)
            y = session.get('y')
            rjson1 = str(user.UserKeypair.gamma) + ',' + str(xi) + ',' + str(orig_z) + ',' + str(zu) + ',' + str(y)
            
            print(rjson1)
            """
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
            """
            return rjson1
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
            
            secp = session.get('secp')
        
            if secp == 'secp256k1':
                params = blind_demo.choose_parameters_secp256k1()
            elif secp == 'secp192k1':
                params = blind_demo.choose_parameters_secp192k1()
            elif secp == 'secp160k1':
                params = blind_demo.choose_parameters_secp160k1()
            
            orig_gamma = blind_demo.getObjFromSession('gamma_bytes',params.group)
            orig_h = blind_demo.getObjFromSession('h_bytes',params.group)
            orig_g = blind_demo.getObjFromSession('g_bytes',params.group)
            
            
            x = session.get('x')
            y = session.get('y')
            
            z = session.get('z')
            
            
            tracerparams = blind_demo.tracer_choose_keypair(params.group,orig_g)
            xt = tracerparams.yt
            yt = tracerparams.yt
            
            session['xt'] = str(xt)
            session['yt'] = str(yt)
            
            upsilon = session.get('upsilon')
            mu = session.get('mu')
            d = session.get('d')
            s1 = session.get('s1')
            s2 = session.get('s2')
            
            issuer = blind_demo.Issuer(orig_g,orig_h,x,y,params)
            issuer.start(z,upsilon,mu,d,s1,s2, yt)
            
            return issuer
    except Exception:
        return None
    

    
def getUserObj():
    try:
            
            secp = session.get('secp')
        
            if secp == 'secp256k1':
                params = blind_demo.choose_parameters_secp256k1()
            elif secp == 'secp192k1':
                params = blind_demo.choose_parameters_secp192k1()
            elif secp == 'secp160k1':
                params = blind_demo.choose_parameters_secp160k1()
            
            orig_g = blind_demo.getObjFromSession('g_bytes',params.group)
            orig_h = blind_demo.getObjFromSession('h_bytes',params.group)
            orig_z = blind_demo.getObjFromSession('z_bytes',params.group)
            orig_gamma = blind_demo.getObjFromSession('gamma_bytes',params.group)
            orig_xi = blind_demo.getObjFromSession('xi_bytes',params.group)
            
            orig_t1 = blind_demo.getObjFromSession('t1_bytes',params.group)
            orig_t2 = blind_demo.getObjFromSession('t2_bytes',params.group)
            orig_t3 = blind_demo.getObjFromSession('t3_bytes',params.group)
            orig_t4 = blind_demo.getObjFromSession('t4_bytes',params.group)
            orig_t5 = blind_demo.getObjFromSession('t5_bytes',params.group)
            orig_y = blind_demo.getObjFromSession('y_bytes',params.group)
            
            user = blind_demo.User(orig_g,orig_h,orig_gamma,orig_xi,params)
            user.start( orig_t1, orig_t2, orig_t3, orig_t4, orig_t5, orig_z, orig_y)
            
            return user
    except Exception:
        return None
    