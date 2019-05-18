#author:rujia
#website:www.rujia.uk
#version:1.0

from flask import session,request,render_template
from . import app
from core import blind_demo
from core import until


@app.route('/issuing')
def issuing():
    yt = str(request.args.get('pk'))
    contractAddress = str(request.args.get('contractAddress'))
    session['yt'] = yt
    session['cas'] = contractAddress
    
    return render_template('issuing.html')

@app.route("/initgamma", methods=['GET'])
def initgamma():
    try:
            secp = session.get('secp')
        
            if secp == 'secp256k1':
                params = blind_demo.choose_parameters_secp256k1()
            elif secp == 'secp192k1':
                params = blind_demo.choose_parameters_secp192k1()
            elif secp == 'secp160k1':
                params = blind_demo.choose_parameters_secp160k1()
            
            orig_z = until.getObjFromSession('z_bytes',params.group)
            orig_zu = until.getObjFromSession('zu_bytes',params.group)
            orig_xi = until.getObjFromSession('xi_bytes',params.group)
            orig_gamma = until.getObjFromSession('gamma_bytes',params.group)
            orig_y = until.getObjFromSession('y_bytes',params.group)
            
            rjson1 = str(orig_gamma) + '#' + str(orig_xi) + '#' + str(orig_z) + '#' + str(orig_zu) + '#' + str(orig_y)
            
            orig_zu = until.getObjFromSession('zu_bytes',params.group)
            
            # protocol two
            orig_upsilon = until.getObjFromSession('upsilon_bytes',params.group)
            orig_mu = until.getObjFromSession('mu_bytes',params.group)
            orig_d = until.getObjFromSession('d_bytes',params.group)
            orig_s1 = until.getObjFromSession('s1_bytes',params.group)
            orig_s2 = until.getObjFromSession('s2_bytes',params.group)
            orig_z1 = until.getObjFromSession('z1_bytes',params.group)
            orig_z2 = until.getObjFromSession('z2_bytes',params.group)
            orig_a = until.getObjFromSession('a_bytes',params.group)
            orig_b1 = until.getObjFromSession('b1_bytes',params.group)
            orig_b2 = until.getObjFromSession('b2_bytes',params.group)
            
            rjson2 = str(orig_upsilon) + '#' + str(orig_mu) + '#' + str(orig_d) + '#' + str(orig_s1) + '#' + str(orig_s2) + '#' + str(orig_z1) + '#' + str(orig_z2) + '#' + str(orig_a)+ '#' + str(orig_b1)+ '#' + str(orig_b2)
            
            # protocol three
            
            orig_t1 = until.getObjFromSession('t1_bytes',params.group)
            orig_t2 = until.getObjFromSession('t2_bytes',params.group)
            orig_t3 = until.getObjFromSession('t3_bytes',params.group)
            orig_t4 = until.getObjFromSession('t4_bytes',params.group)
            orig_t5 = until.getObjFromSession('t5_bytes',params.group)
            
            orig_zeta1 = until.getObjFromSession('zeta1_bytes',params.group)
            orig_zeta2 = until.getObjFromSession('zeta2_bytes',params.group)
            orig_alpha = until.getObjFromSession('alpha_bytes',params.group)
            orig_beta1 = until.getObjFromSession('beta1_bytes',params.group)
            orig_beta2 = until.getObjFromSession('beta2_bytes',params.group)
            orig_epsilon = until.getObjFromSession('epsilon_bytes',params.group)
            orig_e = until.getObjFromSession('e_bytes',params.group)
            
            rjson3 = str(orig_t1) + '#' + str(orig_t2) + '#' + str(orig_t3) + '#' + str(orig_t4) + '#' + str(orig_t5) + '#' + str(orig_zeta1) + '#' + str(orig_zeta2) + '#' + str(orig_alpha)+ '#' + str(orig_b1)+ '#' + str(orig_beta1)+ '#' + str(orig_beta2)+ '#' + str(orig_epsilon)+ '#' + str(orig_e)

            rjson = rjson1 + '#' + rjson2 + '#' + rjson3
            
            # protocol four
            orig_c = until.getObjFromSession('c_bytes',params.group)
            orig_r = until.getObjFromSession('r_bytes',params.group)
            
            rjson4 = str(orig_c) + '#' + str(orig_r)
            
            # protocol five
            orig_rho = until.getObjFromSession('rho_bytes',params.group)
            orig_omega = until.getObjFromSession('omega_bytes',params.group)
            orig_sigma1 = until.getObjFromSession('sigma1_bytes',params.group)
            orig_sigma2 = until.getObjFromSession('sigma2_bytes',params.group)
            orig_delta = until.getObjFromSession('delta_bytes',params.group)
            
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
            
            until.putBytesToSession('upsilon_bytes',upsilon, params.group)
            until.putBytesToSession('mu_bytes' ,mu, params.group)
            until.putBytesToSession('s1_bytes' ,s1, params.group)
            until.putBytesToSession('s2_bytes' ,s2, params.group)
            until.putBytesToSession('d_bytes' ,d, params.group)
            
            rjson = str(upsilon) + '#' + str(mu) + '#' + str(s1) + '#' + str(s2) + '#' + str(d)
            return rjson
        
    except Exception as e:
        print(e)
        return "0"

#issuer 's 

@app.route("/issuerExecuteTwo", methods=['GET'])
def issuerExecuteTwo():
    try:
            issuer = getIssuerObj()
            
            orig_zu = until.getObjFromSession('zu_bytes',issuer.parameters.group)
            orig_upsilon = until.getObjFromSession('upsilon_bytes',issuer.parameters.group)
            orig_mu = until.getObjFromSession('mu_bytes',issuer.parameters.group)
            orig_s1 = until.getObjFromSession('s1_bytes',issuer.parameters.group)
            orig_s2 = until.getObjFromSession('s2_bytes',issuer.parameters.group)
            orig_d = until.getObjFromSession('d_bytes',issuer.parameters.group)
            
            tracerparams = blind_demo.tracer_choose_keypair(issuer.parameters.group,issuer.g)
            xt = tracerparams.yt
            yt = tracerparams.yt
            until.putBytesToSession('xt_bytes', xt, issuer.parameters.group)
            until.putBytesToSession('yt_bytes', yt, issuer.parameters.group)
            
            z1, z2, a, b1, b2 = issuer.protocol_two(yt,orig_upsilon,orig_zu,orig_mu,orig_s1,orig_s2,orig_d)
            
            until.putBytesToSession('z1_bytes', z1, issuer.parameters.group)
            until.putBytesToSession('z2_bytes', z2, issuer.parameters.group)
            until.putBytesToSession('a_bytes', a, issuer.parameters.group)
            until.putBytesToSession('b1_bytes', b1, issuer.parameters.group)
            until.putBytesToSession('b2_bytes', b2, issuer.parameters.group)
            
            rjson = str(z1) + '#' + str(z2) + '#' + str(a) + '#' + str(b1)+ '#' + str(b2)
            
            return rjson
    except Exception as e:
        print(e)
        return "0"

@app.route("/issuerExecuteFour", methods=['GET'])
def issuerExecuteFour():
    try:
            issuer = getIssuerObj()
            
            orig_e = until.getObjFromSession('e_bytes',issuer.parameters.group)
            orig_d = until.getObjFromSession('d_bytes',issuer.parameters.group)
            orig_mu = until.getObjFromSession('mu_bytes',issuer.parameters.group)
            
            r,c = issuer.protocol_four(orig_e, orig_d, orig_mu)
            
            until.putBytesToSession('r_bytes',r, issuer.parameters.group)
            until.putBytesToSession('c_bytes',c, issuer.parameters.group)
            
            rjson = str(r) + ',' + str(c)
            return rjson
    except Exception as e:
        print(e)
        return "0"    

@app.route("/issuerExecuteSix", methods=['GET'])
def issuerExecuteSix():
    try:
            contractAddress = session.get('cas')
            issuer = getIssuerObj()
            orig_xi = until.getObjFromSession('xi_bytes',issuer.parameters.group)
            orig_upsilon = until.getObjFromSession('upsilon_bytes',issuer.parameters.group)
            
            xiupsilon = issuer.protocol_six(orig_xi, orig_upsilon)
            until.putBytesToSession('xiupsilon_bytes',xiupsilon, issuer.parameters.group)
            
            rjson  = str(orig_xi) + "," + str(xiupsilon) + "," + str(contractAddress)
            return rjson
        
    except Exception as e:
        print(e)
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
            
            orig_h = until.getObjFromSession('h_bytes',params.group)
            orig_g = until.getObjFromSession('g_bytes',params.group)
            orig_x = until.getObjFromSession('x_bytes',params.group)
            orig_y = until.getObjFromSession('y_bytes',params.group)
            orig_z = until.getObjFromSession('z_bytes',params.group)
            
            issuer = blind_demo.Issuer(orig_g,orig_h,orig_x,orig_y,orig_z,params)
            
            """
            if session.get('upsilon_bytes')!=None:
                orig_upsilon = until.getObjFromSession('upsilon_bytes',params.group)
                
            if session.get('mu_bytes')!=None:
                orig_mu = until.getObjFromSession('mu_bytes',params.group)
                
            if session.get('d_bytes')!=None:
                orig_d = until.getObjFromSession('d_bytes',params.group)
                
            if session.get('s1_bytes')!=None:
                orig_s1 = until.getObjFromSession('s1_bytes',params.group)
                
            if session.get('s2_bytes')!=None:
                orig_s2 = until.getObjFromSession('s2_bytes',params.group)
            
            issuer.start(orig_z,orig_upsilon,orig_mu,orig_d,orig_s1,orig_s2)
            """
            
            
            return issuer
    except Exception:
        return None