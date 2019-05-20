#author:rujia
#website:www.rujia.uk
#version:1.0

from flask import session,render_template
from . import app
#from . import db
from core import blind_demo
from core import until

@app.route('/verifying')
def verifying():
    return render_template('verifying.html')

@app.route("/getCred", methods=['GET'])
def getCred():
    try:

            uid = until.get_mac_address()
            print("-----------------")
            print(uid)
            print("-----------------")
            secp = session.get(uid+'secp')
        
            if secp == 'secp256k1':
                params = blind_demo.choose_parameters_secp256k1()
            elif secp == 'secp192k1':
                params = blind_demo.choose_parameters_secp192k1()
            
            
            orig_y = until.getObjFromSession(uid+'y_bytes',params.group)
            orig_zeta1 = until.getObjFromSession(uid+'zeta1_bytes',params.group)
            orig_omega = until.getObjFromSession(uid+'omega_bytes',params.group)
            orig_sigma1 = until.getObjFromSession(uid+'sigma1_bytes',params.group)
            orig_sigma2 = until.getObjFromSession(uid+'sigma2_bytes',params.group)
            orig_delta = until.getObjFromSession(uid+'delta_bytes',params.group)
            orig_rho = until.getObjFromSession(uid+'rho_bytes',params.group)
            
            m = session.get(uid+'m')
            
            rjson = str(orig_y) + '#' + str(orig_zeta1) + '#' + str(orig_rho)+ '#' + str(orig_omega)+ '#' + str(orig_sigma1)+ '#' + str(orig_sigma2)+ '#' + str(orig_delta)+ '#' + str(m)
            
            return rjson
    except Exception as e:
        return "0"
    
@app.route("/verifyCred", methods=['GET'])
def verifyCred():
    try:
            uid = until.get_mac_address()
            secp = session.get(uid+'secp')
        
            if secp == 'secp256k1':
                params = blind_demo.choose_parameters_secp256k1()
            elif secp == 'secp192k1':
                params = blind_demo.choose_parameters_secp192k1()
            
            m = session.get(uid+'m')
            
            orig_y = until.getObjFromSession(uid+'y_bytes',params.group)
            orig_zeta1 = until.getObjFromSession(uid+'zeta1_bytes',params.group)
            orig_zeta2 = until.getObjFromSession(uid+'zeta2_bytes',params.group)
            orig_omega = until.getObjFromSession(uid+'omega_bytes',params.group)
            orig_sigma1 = until.getObjFromSession(uid+'sigma1_bytes',params.group)
            orig_sigma2 = until.getObjFromSession(uid+'sigma2_bytes',params.group)
            orig_delta = until.getObjFromSession(uid+'delta_bytes',params.group)
            orig_rho = until.getObjFromSession(uid+'rho_bytes',params.group)
            orig_z = until.getObjFromSession(uid+'z_bytes',params.group)
            orig_g = until.getObjFromSession(uid+'g_bytes',params.group)
            orig_h = until.getObjFromSession(uid+'h_bytes',params.group)
            
            alpha_bytes = until.getObjFromSession(uid+'alpha_bytes',params.group)
            beta1_bytes = until.getObjFromSession(uid+'beta1_bytes',params.group)
            beta2_bytes = until.getObjFromSession(uid+'beta2_bytes',params.group)
            print("alpha_bytes", alpha_bytes)
            print("beta1_bytes", beta1_bytes)
            print("beta2_bytes", beta2_bytes)
            
            lhs, rhs = blind_demo.verify(orig_rho, orig_omega, orig_delta, orig_sigma1,orig_sigma2, orig_h,orig_g, m, orig_y, orig_zeta1, orig_zeta2,orig_z,params)
            
            rjson = str(lhs)  + ',' + str(rhs)
            
            return rjson
    except Exception as e:
        print(e)
        return "0"