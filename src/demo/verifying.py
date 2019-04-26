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
            y = session.get('y')
            zeta1 = session.get('zeta1')
            rho = session.get('rho')
            omega = session.get('omega')
            sigma1 = session.get('sigma1')
            sigma2 = session.get('sigma2')
            delta = session.get('delta')
            m = session.get('m')
            
            rjson = str(y) + ',' + str(zeta1) + ',' + str(rho)+ ',' + str(omega)+ ',' + str(sigma1)+ ',' + str(sigma2)+ ',' + str(delta)+ ',' + str(m)
            
            return rjson
    except Exception as e:
        return "0"
    
@app.route("/verifyCred", methods=['GET'])
def verifyCred():
    try:
            y = session.get('y')
            zeta1 = session.get('zeta1')
            zeta2 = session.get('zeta2')
            z = session.get('z')
            m = session.get('m')
            
            rho = session.get('rho')
            sigma1 = session.get('sigma1')
            sigma2 = session.get('sigma2')
            omega = session.get('omega')
            delta = session.get('delta')
            
            L = session.get('L')
            N = session.get('N')
            p = session.get('p')
            q = session.get('q')
            g = session.get('g')
            h = session.get('h')
            
            params = blind_demo.Parameters(L, N, p, q, g, h)
            
            lhs, rhs = blind_demo.verify(rho, omega, delta, sigma1,sigma2, h, m, y, zeta1, zeta2,z,params)
            
            rjson = str(lhs)  + ',' + str(rhs)
            
            return rjson
    except Exception as e:
        print(e)
        return "0"