#author:rujia
#website:www.rujia.uk
#version:1.0

from flask import session,render_template
from . import app
#from . import db
from core import blind_demo

@app.route('/verifying')
def verifying():
    return render_template('verifying.html')

@app.route("/getCred", methods=['GET'])
def getCred():
    try:

            secp = session.get('secp')
        
            if secp == 'secp256k1':
                params = blind_demo.choose_parameters_secp256k1()
            elif secp == 'secp192k1':
                params = blind_demo.choose_parameters_secp192k1()
            elif secp == 'secp160k1':
                params = blind_demo.choose_parameters_secp160k1()
            
            orig_y = blind_demo.getObjFromSession('y_bytes',params.group)
            orig_zeta1 = blind_demo.getObjFromSession('zeta1_bytes',params.group)
            orig_omega = blind_demo.getObjFromSession('omega_bytes',params.group)
            orig_sigma1 = blind_demo.getObjFromSession('sigma1_bytes',params.group)
            orig_sigma2 = blind_demo.getObjFromSession('sigma2_bytes',params.group)
            orig_delta = blind_demo.getObjFromSession('delta_bytes',params.group)
            orig_rho = blind_demo.getObjFromSession('rho_bytes',params.group)
            
            m = session.get('m')
            
            rjson = str(orig_y) + '#' + str(orig_zeta1) + '#' + str(orig_rho)+ '#' + str(orig_omega)+ '#' + str(orig_sigma1)+ '#' + str(orig_sigma2)+ '#' + str(orig_delta)+ '#' + str(m)
            
            return rjson
    except Exception as e:
        return "0"
    
@app.route("/verifyCred", methods=['GET'])
def verifyCred():
    try:
            secp = session.get('secp')
        
            if secp == 'secp256k1':
                params = blind_demo.choose_parameters_secp256k1()
            elif secp == 'secp192k1':
                params = blind_demo.choose_parameters_secp192k1()
            elif secp == 'secp160k1':
                params = blind_demo.choose_parameters_secp160k1()
            
            
            m = session.get('m')
            
            orig_y = blind_demo.getObjFromSession('y_bytes',params.group)
            orig_zeta1 = blind_demo.getObjFromSession('zeta1_bytes',params.group)
            orig_zeta2 = blind_demo.getObjFromSession('zeta2_bytes',params.group)
            orig_omega = blind_demo.getObjFromSession('omega_bytes',params.group)
            orig_sigma1 = blind_demo.getObjFromSession('sigma1_bytes',params.group)
            orig_sigma2 = blind_demo.getObjFromSession('sigma2_bytes',params.group)
            orig_delta = blind_demo.getObjFromSession('delta_bytes',params.group)
            orig_rho = blind_demo.getObjFromSession('rho_bytes',params.group)
            orig_z = blind_demo.getObjFromSession('z_bytes',params.group)
            orig_g = blind_demo.getObjFromSession('g_bytes',params.group)
            orig_h = blind_demo.getObjFromSession('h_bytes',params.group)
            
            
            lhs, rhs = blind_demo.verify(orig_rho, orig_omega, orig_delta, orig_sigma1,orig_sigma2, orig_h,orig_g, m, orig_y, orig_zeta1, orig_zeta2,orig_z,params)
            
            rjson = str(lhs)  + ',' + str(rhs)
            
            return rjson
    except Exception as e:
        print(e)
        return "0"