#author:rujia
#website:www.rujia.uk
#version:1.0

from flask import session,request
from . import app
from core import blind_demo
from core import until

@app.route("/setParamsUser", methods=['GET'])
def setParamsUser():
    try:
            uid = until.get_mac_address()
            secp = session.get(uid+'secp')
            if secp == 'secp256k1':
                params = blind_demo.choose_parameters_secp256k1()
            elif secp == 'secp192k1':
                params = blind_demo.choose_parameters_secp192k1()
           
           
            t1, t2, t3, t4, t5 = blind_demo.get_random_ZR(params.group),blind_demo.get_random_ZR(params.group),blind_demo.get_random_ZR(params.group),blind_demo.get_random_ZR(params.group),blind_demo.get_random_ZR(params.group)
            
            until.putBytesToSession(uid+'t1_bytes',t1, params.group)
            until.putBytesToSession(uid+'t2_bytes',t2, params.group)
            until.putBytesToSession(uid+'t3_bytes',t3, params.group)
            until.putBytesToSession(uid+'t4_bytes',t4, params.group)
            until.putBytesToSession(uid+'t5_bytes',t5, params.group)
            
            rjson = str(t1) + '#' + str(t2) + '#' + str(t3) + '#' + str(t4) + '#' + str(t5)
            
            return rjson
    except Exception as e:
        print(e)
        return "0"

@app.route("/userExecuteOne", methods=['POST'])
def userExecuteOne():
    try:
            user = getUserObj()
            uid = until.get_mac_address()
            orig_z = until.getObjFromSession(uid+'z_bytes',user.parameters.group)
            orig_gamma = until.getObjFromSession(uid+'gamma_bytes',user.parameters.group)
            #z = until.point2Obj(39972701138670676199833069686228758314468515773606341811291326318149542933708, user.parameters.group)
            #gamma = until.unmber2Obj(67950487539194343191118481106849796541317734897587234319291961516724185583159, user.parameters.group)
            zu = user.protocol_one(orig_z, orig_gamma)
            until.putBytesToSession(uid+'zu_bytes', zu, user.parameters.group)
            
            rjson = str(user.UserKeypair.gamma) + '#' + str(user.UserKeypair.xi)+ '#' + str(orig_z) + '#' + str(zu)
            return rjson
    except Exception as e1:
        print(e1)
        return "0"


@app.route("/userExecuteThree", methods=['POST'])
def userExecuteThree():
    try:
            uid = until.get_mac_address()
            m = str(request.form['m'])
            m = bytes(m,'utf-8')
            session[uid+'m'] = m
            
            user = getUserObj()
            orig_z1 = until.getObjFromSession(uid+'z1_bytes',user.parameters.group)
            orig_a = until.getObjFromSession(uid+'a_bytes',user.parameters.group)
            orig_b1 = until.getObjFromSession(uid+'b1_bytes',user.parameters.group)
            orig_b2 = until.getObjFromSession(uid+'b2_bytes',user.parameters.group)
            
            orig_t1 = until.getObjFromSession(uid+'t1_bytes',user.parameters.group)
            orig_t2 = until.getObjFromSession(uid+'t2_bytes',user.parameters.group)
            orig_t3 = until.getObjFromSession(uid+'t3_bytes',user.parameters.group)
            orig_t4 = until.getObjFromSession(uid+'t4_bytes',user.parameters.group)
            orig_t5 = until.getObjFromSession(uid+'t5_bytes',user.parameters.group)
            
            orig_y = until.getObjFromSession(uid+'y_bytes',user.parameters.group)
            
            zeta1, zeta2, alpha, beta1, beta2, epsilon, e = user.protocol_three(orig_z1, orig_a, orig_b1, orig_b2, m, orig_y,orig_t1, orig_t2, orig_t3, orig_t4, orig_t5)
            
            until.putBytesToSession(uid+'zeta1_bytes',zeta1, user.parameters.group)
            until.putBytesToSession(uid+'zeta2_bytes',zeta2, user.parameters.group)
            until.putBytesToSession(uid+'alpha_bytes',alpha, user.parameters.group)
            until.putBytesToSession(uid+'beta1_bytes',beta1, user.parameters.group)
            until.putBytesToSession(uid+'beta2_bytes',beta2, user.parameters.group)
            until.putBytesToSession(uid+'epsilon_bytes',epsilon, user.parameters.group)
            until.putBytesToSession(uid+'e_bytes',e, user.parameters.group)
            
            rjson = str(zeta1) + '#' + str(zeta2) + '#' + str(alpha)+ '#' + str(beta1)+ '#' + str(beta2)+ '#' + str(epsilon)+ '#' + str(e)
            return rjson
        
    except Exception as exception:
        print(exception)
        return "0"
  
@app.route("/userExecuteFive", methods=['GET'])
def userExecuteFive():
    try:
            user = getUserObj()
            
            uid = until.get_mac_address()
           
            orig_r = until.getObjFromSession(uid+'r_bytes',user.parameters.group)
            orig_c = until.getObjFromSession(uid+'c_bytes',user.parameters.group)
            orig_s1 = until.getObjFromSession(uid+'s1_bytes',user.parameters.group)
            orig_s2 = until.getObjFromSession(uid+'s2_bytes',user.parameters.group)
            orig_d = until.getObjFromSession(uid+'d_bytes',user.parameters.group)
            
            orig_t1 = until.getObjFromSession(uid+'t1_bytes',user.parameters.group)
            orig_t2 = until.getObjFromSession(uid+'t2_bytes',user.parameters.group)
            orig_t3 = until.getObjFromSession(uid+'t3_bytes',user.parameters.group)
            orig_t4 = until.getObjFromSession(uid+'t4_bytes',user.parameters.group)
            orig_t5 = until.getObjFromSession(uid+'t5_bytes',user.parameters.group)
            
            rho, omega, sigma1, sigma2, delta = user.protocol_five(orig_r, orig_c, orig_s1, orig_s2, orig_d, orig_t1, orig_t2, orig_t3, orig_t4, orig_t5)
            
            until.putBytesToSession(uid+'rho_bytes',rho, user.parameters.group)
            until.putBytesToSession(uid+'omega_bytes',omega, user.parameters.group)
            until.putBytesToSession(uid+'sigma1_bytes',sigma1, user.parameters.group)
            until.putBytesToSession(uid+'sigma2_bytes',sigma2, user.parameters.group)
            until.putBytesToSession(uid+'delta_bytes',delta, user.parameters.group)
            
            rjson = str(rho) + '#' + str(omega) + '#' + str(sigma1) + '#' + str(sigma2) + '#' + str(delta)
            
            return rjson
    except Exception as e1:
        print(e1)
        return "0"

def getUserObj():
    try:
            uid = until.get_mac_address()
            secp = session.get(uid+'secp')
        
            if secp == 'secp256k1':
                params = blind_demo.choose_parameters_secp256k1()
            elif secp == 'secp192k1':
                params = blind_demo.choose_parameters_secp192k1()
            
            
            if session.get(uid+'g_bytes')!=None:
                orig_g = until.getObjFromSession(uid+'g_bytes',params.group)
            if session.get(uid+'h_bytes')!=None:
                orig_h = until.getObjFromSession(uid+'h_bytes',params.group)
            if session.get(uid+'z_bytes')!=None:
                orig_z = until.getObjFromSession(uid+'z_bytes',params.group)
            if session.get(uid+'gamma_bytes')!=None:
                orig_gamma = until.getObjFromSession(uid+'gamma_bytes',params.group)
            if session.get(uid+'xi_bytes')!=None:
                orig_xi = until.getObjFromSession(uid+'xi_bytes',params.group)
            
            user = blind_demo.User(orig_g,orig_h,orig_z,orig_gamma,orig_xi,params)
            
            """
            if session.get('t1_bytes')!=None:
                orig_t1 = until.getObjFromSession('t1_bytes',params.group)
            if session.get('t2_bytes')!=None:
                orig_t2 = until.getObjFromSession('t2_bytes',params.group)
            if session.get('t3_bytes')!=None:
                orig_t3 = until.getObjFromSession('t3_bytes',params.group)
            if session.get('t4_bytes')!=None:
                orig_t4 = until.getObjFromSession('t4_bytes',params.group)
            if session.get('t5_bytes')!=None:
                orig_t5 = until.getObjFromSession('t5_bytes',params.group)
            if session.get('y_bytes')!=None:
                orig_y = until.getObjFromSession('y_bytes',params.group)
            """  
            return user
    except Exception:
        return None
    