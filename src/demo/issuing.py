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
            
            secp = session.get('secp')
            print(secp)
        
            if secp == 'secp256k1':
                params = blind_demo.choose_parameters_secp256k1()
            elif secp == 'secp192k1':
                params = blind_demo.choose_parameters_secp192k1()
            elif secp == 'secp160k1':
                params = blind_demo.choose_parameters_secp160k1()
            
            orig_z = blind_demo.getObjFromSession('z_bytes',params.group)
            orig_zu = blind_demo.getObjFromSession('zu_bytes',params.group)
            orig_xi = blind_demo.getObjFromSession('xi_bytes',params.group)
            orig_gamma = blind_demo.getObjFromSession('gamma_bytes',params.group)
            orig_y = blind_demo.getObjFromSession('y_bytes',params.group)
            
            rjson1 = str(orig_gamma) + '#' + str(orig_xi) + '#' + str(orig_z) + '#' + str(orig_zu) + '#' + str(orig_y)
            
            
            orig_zu = blind_demo.getObjFromSession('zu_bytes',params.group)
            
            
            # protocol two
            orig_upsilon = blind_demo.getObjFromSession('upsilon_bytes',params.group)
            orig_mu = blind_demo.getObjFromSession('mu_bytes',params.group)
            orig_d = blind_demo.getObjFromSession('d_bytes',params.group)
            orig_s1 = blind_demo.getObjFromSession('s1_bytes',params.group)
            orig_s2 = blind_demo.getObjFromSession('s2_bytes',params.group)
            orig_z1 = blind_demo.getObjFromSession('z1_bytes',params.group)
            orig_z2 = blind_demo.getObjFromSession('z2_bytes',params.group)
            orig_a = blind_demo.getObjFromSession('a_bytes',params.group)
            orig_b1 = blind_demo.getObjFromSession('b1_bytes',params.group)
            orig_b2 = blind_demo.getObjFromSession('b2_bytes',params.group)
            
            rjson2 = str(orig_upsilon) + '#' + str(orig_mu) + '#' + str(orig_d) + '#' + str(orig_s1) + '#' + str(orig_s2) + '#' + str(orig_z1) + '#' + str(orig_z2) + '#' + str(orig_a)+ '#' + str(orig_b1)+ '#' + str(orig_b2)
            
            # protocol three
            
            orig_t1 = blind_demo.getObjFromSession('t1_bytes',params.group)
            orig_t2 = blind_demo.getObjFromSession('t2_bytes',params.group)
            orig_t3 = blind_demo.getObjFromSession('t3_bytes',params.group)
            orig_t4 = blind_demo.getObjFromSession('t4_bytes',params.group)
            orig_t5 = blind_demo.getObjFromSession('t5_bytes',params.group)
            
            orig_zeta1 = blind_demo.getObjFromSession('zeta1_bytes',params.group)
            orig_zeta2 = blind_demo.getObjFromSession('zeta2_bytes',params.group)
            orig_alpha = blind_demo.getObjFromSession('alpha_bytes',params.group)
            orig_beta1 = blind_demo.getObjFromSession('beta1_bytes',params.group)
            orig_beta2 = blind_demo.getObjFromSession('beta2_bytes',params.group)
            orig_epsilon = blind_demo.getObjFromSession('epsilon_bytes',params.group)
            orig_e = blind_demo.getObjFromSession('e_bytes',params.group)
            
            rjson3 = str(orig_t1) + '#' + str(orig_t2) + '#' + str(orig_t3) + '#' + str(orig_t4) + '#' + str(orig_t5) + '#' + str(orig_zeta1) + '#' + str(orig_zeta2) + '#' + str(orig_alpha)+ '#' + str(orig_b1)+ '#' + str(orig_beta1)+ '#' + str(orig_beta2)+ '#' + str(orig_epsilon)+ '#' + str(orig_e)

            rjson = rjson1 + '#' + rjson2 + '#' + rjson3
            
            # protocol four
            orig_c = blind_demo.getObjFromSession('c_bytes',params.group)
            orig_r = blind_demo.getObjFromSession('r_bytes',params.group)
            
            rjson4 = str(orig_c) + '#' + str(orig_r)
            
            # protocol five
            orig_rho = blind_demo.getObjFromSession('rho_bytes',params.group)
            orig_omega = blind_demo.getObjFromSession('omega_bytes',params.group)
            orig_sigma1 = blind_demo.getObjFromSession('sigma1_bytes',params.group)
            orig_sigma2 = blind_demo.getObjFromSession('sigma2_bytes',params.group)
            orig_delta = blind_demo.getObjFromSession('delta_bytes',params.group)
            
            rjson5 = str(orig_rho) + '#' + str(orig_omega) + '#' + str(orig_sigma1) + '#' + str(orig_sigma2) + '#' + str(orig_delta)
            
            rjson = rjson1 + '#' + rjson2 + '#' + rjson3 + '#' + rjson4 + '#' + rjson5
            
            
            m = session.get('m')
            if(m != None):
                m = m.decode('utf-8')
            else:
                m = 'None'
            
            rjson =  rjson + '#' + m
            
            contractAddress = session.get('cas')
            xiupsilon = session.get('xiupsilon')
            
            rjson = rjson + '#' + str(contractAddress) + '#' + str(xiupsilon)
            
            return rjson
    except Exception:
        return "0"
    

@app.route("/issuerExecuteTwo", methods=['GET'])
def issuerExecuteTwo():
    try:
            issuer = getIssuerObj()
            orig_zu = blind_demo.getObjFromSession('zu_bytes',issuer.parameters.group)
            
            tracerparams = blind_demo.tracer_choose_keypair(issuer.parameters.group,issuer.g)
            xt = tracerparams.yt
            yt = tracerparams.yt
            
            blind_demo.putBytesToSession('xt_bytes', xt, issuer.parameters.group)
            blind_demo.putBytesToSession('yt_bytes', yt, issuer.parameters.group)
            issuer.tkey = yt
            
            issuer.protocol_two(orig_zu)
            
            blind_demo.putBytesToSession('z1_bytes', issuer.z1, issuer.parameters.group)
            blind_demo.putBytesToSession('z2_bytes', issuer.z2, issuer.parameters.group)
            blind_demo.putBytesToSession('a_bytes', issuer.a, issuer.parameters.group)
            blind_demo.putBytesToSession('b1_bytes', issuer.b1, issuer.parameters.group)
            blind_demo.putBytesToSession('b2_bytes', issuer.b2, issuer.parameters.group)
            
            rjson = str(issuer.z1) + '#' + str(issuer.z2) + '#' + str(issuer.a) + '#' + str(issuer.b1)+ '#' + str(issuer.b2)
            
            
            
            return rjson
    except Exception as e:
        print(e)
        return "0"

@app.route("/setParamsIssuer", methods=['GET'])
def setParamsIssuer():
    try:
            
            secp = session.get('secp')
        
            if secp == 'secp256k1':
                params = blind_demo.choose_parameters_secp256k1()
            elif secp == 'secp192k1':
                params = blind_demo.choose_parameters_secp192k1()
            elif secp == 'secp160k1':
                params = blind_demo.choose_parameters_secp160k1()
           
            upsilon, mu, s1, s2, d = blind_demo.get_random_ZR(params.group),blind_demo.get_random_ZR(params.group),blind_demo.get_random_ZR(params.group),blind_demo.get_random_ZR(params.group),blind_demo.get_random_ZR(params.group)
            
            blind_demo.putBytesToSession('upsilon_bytes',upsilon, params.group)
            blind_demo.putBytesToSession('mu_bytes',mu, params.group)
            blind_demo.putBytesToSession('s1_bytes',s1, params.group)
            blind_demo.putBytesToSession('s2_bytes',s2, params.group)
            blind_demo.putBytesToSession('d_bytes',d, params.group)
            
            rjson = str(upsilon) + '#' + str(mu) + '#' + str(s1) + '#' + str(s2) + '#' + str(d)
            
            return rjson
    except Exception as e:
        print(e)
        return "0"

@app.route("/setParamsUser", methods=['GET'])
def setParamsUser():
    try:
            
            secp = session.get('secp')
        
            if secp == 'secp256k1':
                params = blind_demo.choose_parameters_secp256k1()
            elif secp == 'secp192k1':
                params = blind_demo.choose_parameters_secp192k1()
            elif secp == 'secp160k1':
                params = blind_demo.choose_parameters_secp160k1()
           
            t1, t2, t3, t4, t5 = blind_demo.get_random_ZR(params.group),blind_demo.get_random_ZR(params.group),blind_demo.get_random_ZR(params.group),blind_demo.get_random_ZR(params.group),blind_demo.get_random_ZR(params.group)
            
            blind_demo.putBytesToSession('t1_bytes',t1, params.group)
            blind_demo.putBytesToSession('t2_bytes',t2, params.group)
            blind_demo.putBytesToSession('t3_bytes',t3, params.group)
            blind_demo.putBytesToSession('t4_bytes',t4, params.group)
            blind_demo.putBytesToSession('t5_bytes',t5, params.group)
            
            rjson = str(t1) + '#' + str(t2) + '#' + str(t3) + '#' + str(t4) + '#' + str(t5)
            
            return rjson
    except Exception as e:
        print(e)
        return "0"

@app.route("/userExecuteOne", methods=['POST'])
def userExecuteOne():
    try:
            user = getUserObj()
            zu = user.protocol_one()
            blind_demo.putBytesToSession('zu_bytes',zu, user.parameters.group)
            
            orig_z = blind_demo.getObjFromSession('z_bytes',user.parameters.group)
            rjson = str(user.UserKeypair.gamma) + '#' + str(user.UserKeypair.xi)+ '#' + str(orig_z) + '#' + str(zu)
            return rjson
    except Exception as e1:
        print(e1)
        return "0"


@app.route("/userExecuteThree", methods=['POST'])
def userExecuteThree():
    try:
            user = getUserObj()
            
            orig_z1 = blind_demo.getObjFromSession('z1_bytes',user.parameters.group)
            orig_a = blind_demo.getObjFromSession('a_bytes',user.parameters.group)
            orig_b1 = blind_demo.getObjFromSession('b1_bytes',user.parameters.group)
            orig_b2 = blind_demo.getObjFromSession('b2_bytes',user.parameters.group)
            
            
            m = str(request.form['m'])
            
            m = bytes(m,'utf-8')
            session['m'] = m
            
            user.protocol_three(orig_z1, orig_a, orig_b1, orig_b2, m)
            
            blind_demo.putBytesToSession('zeta1_bytes',user.zeta1, user.parameters.group)
            blind_demo.putBytesToSession('zeta2_bytes',user.zeta2, user.parameters.group)
            blind_demo.putBytesToSession('alpha_bytes',user.alpha, user.parameters.group)
            blind_demo.putBytesToSession('beta1_bytes',user.beta1, user.parameters.group)
            blind_demo.putBytesToSession('beta2_bytes',user.beta2, user.parameters.group)
            blind_demo.putBytesToSession('epsilon_bytes',user.epsilon, user.parameters.group)
            blind_demo.putBytesToSession('e_bytes',user.e, user.parameters.group)
            
            rjson = str(user.zeta1) + ',' + str(user.zeta2) + ',' + str(user.alpha)+ ',' + str(user.beta1)+ ',' + str(user.beta2)+ ',' + str(user.epsilon)+ ',' + str(user.e)
            
            return rjson
    except Exception as e1:
        print(e1)
        return "0"


@app.route("/issuerExecuteFour", methods=['GET'])
def issuerExecuteFour():
    try:
            issuer = getIssuerObj()
            
            e = blind_demo.getObjFromSession('e_bytes',issuer.parameters.group)
            r,c,_,_,_  = issuer.protocol_four(e)
            
            blind_demo.putBytesToSession('r_bytes',r, issuer.parameters.group)
            blind_demo.putBytesToSession('c_bytes',c, issuer.parameters.group)
            
            rjson = str(r) + ',' + str(c)
            return rjson
    except Exception as e:
        print(e)
        return "0"    

@app.route("/issuerExecuteSix", methods=['GET'])
def issuerExecuteSix():
    try:
            issuer = getIssuerObj()
            orig_xi = blind_demo.getObjFromSession('xi_bytes',issuer.parameters.group)
            
            contractAddress = session.get('cas')
            xiupsilon = issuer.protocol_six(orig_xi)
            blind_demo.putBytesToSession('xiupsilon_bytes',xiupsilon, issuer.parameters.group)
            
            rjson  = str(orig_xi) + "," + str(xiupsilon) + "," + str(contractAddress)
            return rjson
        
    except Exception as e:
        print(e)
        return "0" 
  
@app.route("/userExecuteFive", methods=['GET'])
def userExecuteFive():
    try:
            user = getUserObj()
           
            r = blind_demo.getObjFromSession('r_bytes',user.parameters.group)
            c = blind_demo.getObjFromSession('c_bytes',user.parameters.group)
            s1 = blind_demo.getObjFromSession('s1_bytes',user.parameters.group)
            s2 = blind_demo.getObjFromSession('s2_bytes',user.parameters.group)
            d = blind_demo.getObjFromSession('d_bytes',user.parameters.group)
            
            rho, omega, sigma1, sigma2, delta = user.protocol_five(r, c, s1,s2, d)
            
            blind_demo.putBytesToSession('rho_bytes',rho, user.parameters.group)
            blind_demo.putBytesToSession('omega_bytes',omega, user.parameters.group)
            blind_demo.putBytesToSession('sigma1_bytes',sigma1, user.parameters.group)
            blind_demo.putBytesToSession('sigma2_bytes',sigma2, user.parameters.group)
            blind_demo.putBytesToSession('delta_bytes',delta, user.parameters.group)
            
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
            
            orig_h = blind_demo.getObjFromSession('h_bytes',params.group)
            orig_g = blind_demo.getObjFromSession('g_bytes',params.group)
            
            orig_x = blind_demo.getObjFromSession('x_bytes',params.group)
            orig_y = blind_demo.getObjFromSession('y_bytes',params.group)
            orig_z = blind_demo.getObjFromSession('z_bytes',params.group)
            
            if session.get('upsilon_bytes')!=None:
                orig_upsilon = blind_demo.getObjFromSession('upsilon_bytes',params.group)
                
            if session.get('mu_bytes')!=None:
                orig_mu = blind_demo.getObjFromSession('mu_bytes',params.group)
                
            if session.get('d_bytes')!=None:
                orig_d = blind_demo.getObjFromSession('d_bytes',params.group)
                
            if session.get('s1_bytes')!=None:
                orig_s1 = blind_demo.getObjFromSession('s1_bytes',params.group)
                
            if session.get('s2_bytes')!=None:
                orig_s2 = blind_demo.getObjFromSession('s2_bytes',params.group)
            
            issuer = blind_demo.Issuer(orig_g,orig_h,orig_x,orig_y,params)
            
            issuer.start(orig_z,orig_upsilon,orig_mu,orig_d,orig_s1,orig_s2)
            
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
            
            
            if session.get('g_bytes')!=None:
                orig_g = blind_demo.getObjFromSession('g_bytes',params.group)
            if session.get('h_bytes')!=None:
                orig_h = blind_demo.getObjFromSession('h_bytes',params.group)
            if session.get('z_bytes')!=None:
                orig_z = blind_demo.getObjFromSession('z_bytes',params.group)
            if session.get('gamma_bytes')!=None:
                orig_gamma = blind_demo.getObjFromSession('gamma_bytes',params.group)
            if session.get('xi_bytes')!=None:
                orig_xi = blind_demo.getObjFromSession('xi_bytes',params.group)
            
            if session.get('t1_bytes')!=None:
                orig_t1 = blind_demo.getObjFromSession('t1_bytes',params.group)
            if session.get('t2_bytes')!=None:
                orig_t2 = blind_demo.getObjFromSession('t2_bytes',params.group)
            if session.get('t3_bytes')!=None:
                orig_t3 = blind_demo.getObjFromSession('t3_bytes',params.group)
            if session.get('t4_bytes')!=None:
                orig_t4 = blind_demo.getObjFromSession('t4_bytes',params.group)
            if session.get('t5_bytes')!=None:
                orig_t5 = blind_demo.getObjFromSession('t5_bytes',params.group)
            if session.get('y_bytes')!=None:
                orig_y = blind_demo.getObjFromSession('y_bytes',params.group)
                
            print(4444444)
            
            
            user = blind_demo.User(orig_g,orig_h,orig_gamma,orig_xi,params)
            
            print(user)
            
            print(2222)
            
            print(orig_t1)
            print(orig_t2)
            print(orig_t3)
            print(orig_t4)
            print(orig_t5)
            print(orig_z)
            print(orig_y)
            
            user.start(orig_t1, orig_t2, orig_t3, orig_t4, orig_t5, orig_z, orig_y)
            
            return user
    except Exception:
        return None
    