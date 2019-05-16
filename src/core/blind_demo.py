#author:rujia
#website:www.rujia.uk
#version:1.0

from charm.toolbox.ecgroup import ECGroup,G,ZR
from charm.toolbox.eccurve import secp160k1,secp192k1,secp256k1
from collections import namedtuple
import hashlib
from flask import session
from charm.core.engine.util import objectToBytes, bytesToObject


Parameters = namedtuple('Parameters', ['secp', 'group', 'g', 'h'])
IssuerKeypair = namedtuple('IssuerKeypair', ['x', 'y'])
UserKeypair = namedtuple('UserKeypair', ['gamma', 'xi'])
TracerKeypair = namedtuple('TracerKeypair', ['xt', 'yt', 'parameters'])

def choose_parameters_secp256k1():
    group = ECGroup(secp256k1)
    g, h = group.random(G), group.random(G)
    parameters = Parameters(type, group, g, h)
    return parameters

def choose_parameters_secp192k1():
    group = ECGroup(secp192k1)
    g, h = group.random(G), group.random(G)
    parameters = Parameters(type, group, g, h)
    return parameters

def choose_parameters_secp160k1():
    group = ECGroup(secp160k1)
    g, h = group.random(G), group.random(G)
    parameters = Parameters(type, group, g, h)
    return parameters

def point2Obj(x, group):
    import binascii
    temp_str = hex(x)[2:]
    dict_ecc = {708: 42,
                711: 48,
                714: 64}
    temp_str = (dict_ecc[group.groupType()] - len(temp_str)) * '0' + temp_str
    return group.encode(binascii.a2b_hex(temp_str), include_ctr=True)

def issuer_choose_keypair(group,orig_g):
    x = group.random(ZR)
    y = orig_g ** x
    return IssuerKeypair(x,y)

def user_choose_keypair(group,orig_g):
    gamma = group.random(ZR)
    xi = orig_g ** gamma
    return UserKeypair(gamma, xi)

def get_random_ZR(group):
    random = group.random(ZR)
    return random

def tracer_choose_keypair(group,orig_g):
    xt = group.random(ZR)
    yt = orig_g ** xt
    return UserKeypair(xt, yt)

def gnerate_common_z(group,g,h,y):
    return group.hash((g, h, y), G)

def int_to_bytes(in_int):
    i = in_int
    byte_length = ((i).bit_length() + 7) // 8
    return i.to_bytes(byte_length, 'little')

### Hashing functions ###
def do_hash(data):
    '''hash helper'''
    h = hashlib.sha256()
    h.update(data)
    return h.digest()

def full_domain_hash(data, target_length):
    tl_bytes = target_length // 8
    digest_size = hashlib.sha256().digest_size
    ncycles = (tl_bytes // digest_size) + 1
    out = bytearray()
    for i in range(ncycles):
        out.extend(do_hash(data + int_to_bytes(i)))
    return bytes(out[:tl_bytes])

def digest(data, parameters):
    '''F hash function from paper'''
    hashed = full_domain_hash(data, parameters.L)
    i = int.from_bytes(hashed, byteorder='little') % parameters.p
    return pow(i, (parameters.p - 1)//parameters.q, parameters.p)

### Protocol stuff ###
class Issuer:
    '''Issuer S from the paper'''
    def __init__(self, g, h, x, y,parameters):
        self.parameters = parameters
        self.g, self.h = g,h
        self.IssuerKeypair = IssuerKeypair(x, y)
        
    def start(self,z,upsilon,mu,d,s1,s2):
        self.z = z
        self.upsilon = upsilon
        self.mu = mu
        self.d = d
        self.s1= s1
        self.s2= s2
        
        

    def protocol_two(self,zu):
        
        self.z1 = self.tkey ** self.upsilon
        
        self.z2 = zu / self.z1
        
        print(self.z2)
        
        self.a = self.IssuerKeypair.parameters.g ** self.mu
        
        self.b1 = (self.IssuerKeypair.parameters.g ** self.s1) * (self.z1 ** self.d) 
        
        self.b2 = (self.IssuerKeypair.parameters.h ** self.s2) * (self.z2 ** self.d)
        
        return self.z1, self.a, self.b1, self.b2

    def protocol_four(self, e):
        self.c = (e - self.d) % self.q
        self.r = (self.mu - (self.c * self.IssuerKeypair.x)) % self.q
        return self.r, self.c, self.s1, self.s2, self.d
    
    def protocol_six(self, xi):
        return pow(xi, self.upsilon, self.p)

class User:
    '''User U from the paper'''
    def __init__(self,g,h,gamma,xi,parameters):
        self.parameters = parameters
        self.g, self.h = g,h
        self.UserKeypair = UserKeypair(gamma, xi)
        
    def start(self, t1, t2, t3, t4, t5, z, y):
        self.t1, self.t2, self.t3, self.t4,self.t5 = t1, t2, t3, t4, t5
        self.z = z
        self.y = y
        
    def protocol_one(self):
        self.z_u = self.z ** (self.UserKeypair.gamma ** -1)
        return (self.z_u, self.UserKeypair.xi)

    def protocol_three(self, z1, a, b1, b2, m):
        
        self.zeta1 = pow(z1, self.UserKeypair.gamma, self.p)
        
        #nzeta1 = pow(self.zeta1, self.p - 2,self.p)
        #self.zeta2 = self.zeta1 * nzeta1 % self.p
        
        self.alpha = (a * pow(self.g, self.t1, self.p) *
                 pow(self.y, self.t2, self.p)) % self.p
          
        self.beta1 = (pow(b1, self.UserKeypair.gamma, self.p) *
                pow(self.g, self.t3, self.p) *
                pow(self.zeta1, self.t5, self.p)
                ) % self.p
        
        #zt5 = pow(self.z, self.t5,self.p)
        #nzeta1t5 = pow(pow(self.zeta1,((self.q)-1),self.p), self.t5, self.p)
        
        self.zeta2 = (self.z * pow(self.zeta1,(self.q)-1,self.p)) % self.p
        
        self.beta2 = (pow(b2, self.UserKeypair.gamma, self.p) *
                pow(self.h, self.t4, self.p) *
                pow(self.zeta2,self.t5,self.p)
                ) % self.p

        e_bytes = bytearray()
        for v in (self.zeta1, self.alpha, self.beta1, self.beta2):
            e_bytes.extend(int_to_bytes(v))
       
        e_bytes.extend(m)

        self.epsilon = int.from_bytes(full_domain_hash(e_bytes, self.N), 'little')
        
        self.e = (self.epsilon - self.t2 - self.t5) % self.q
        
        return self.e

    def protocol_five(self, r, c, s1,s2, d):
        rho = (r + self.t1) % self.q
        omega = (c + self.t2) % self.q
        sigma1 = (s1 * self.UserKeypair.gamma + self.t3) % self.q
        sigma2 = (s2 * self.UserKeypair.gamma + self.t4) % self.q
        delta = (d + self.t5) % self.q
#         delta = (d) % self.q
        return rho, omega, sigma1, sigma2, delta

def verify(rho, omega, delta, sigma1,sigma2, h, m, y, zeta1, zeta2,z, parameters):
    '''Signature verification'''
    lhs = (omega + delta) % parameters.q
    
    rhs_one = zeta1
    
    rhs_two = (pow(parameters.g, rho, parameters.p) *
               pow(y, omega, parameters.p)) % parameters.p
               
    rhs_three = (pow(parameters.g, sigma1, parameters.p) *
               pow(zeta1, delta, parameters.p)) % parameters.p
    
    rhs_four = (pow(h, sigma2, parameters.p) *
                pow(zeta2,delta,parameters.p)
               ) % parameters.p
    
    rhs_hash = full_domain_hash(int_to_bytes(rhs_one) + int_to_bytes(rhs_two) +
                                int_to_bytes(rhs_three) + int_to_bytes(rhs_four) + m, parameters.N)
    
    rhs = int.from_bytes(rhs_hash, 'little') % parameters.q
    
    return lhs,rhs

def credential_tracing(xi, upsilon, xt, parameters):
    cred = pow(xi,upsilon * xt, parameters.p)
    #print(cred)
    #print(user.zeta1)
    return cred == user.zeta1

def identity_tracing(zeta1, xt, upsilon ,parameters):
    
    nxt = pow(xt, parameters.q - 2, parameters.q)
    ide = pow(zeta1, nxt, parameters.p)
    print(ide)
    print(pow(user.UserKeypair.xi, upsilon, parameters.p))
    #print(user.zeta1)
    return ide == pow(user.UserKeypair.xi, upsilon, parameters.p)

# tools
def getObjFromSession(key, group):
    value_bytes = session.get(key)
    orig_value = bytesToObject(value_bytes, group)
    return orig_value

def putBytesToSession(key, value, group):
    value_bytes = objectToBytes(value, group)
    session[key] = value_bytes




if __name__ == '__main__':
    #L, N = 1024, 160
    L, N = 256, 40
    
    m = b'my msg'
    
    # prepare the params of 'p', 'q', 'g'
    params = choose_parameters_secp256k1(L, N)
    
    # get the tracer 's public key 
    tracerKeypair = tracer_choose_keypair(params)
    
    tkey = tracerKeypair.yt
    
    xt = tracerKeypair.xt
    
    issuer = Issuer(params,tkey)
    # get the hash 
    issuer.start()
    
    user = User(params, issuer.IssuerKeypair.y,tkey)
    
    user.start()

    zu, xi = user.protocol_one()
    
    z1, a, b1, b2 = issuer.protocol_two(zu)
    
    e = user.protocol_three(z1, a, b1, b2, m)
    
    r, c, s1, s2, d = issuer.protocol_four(e)
    
    rho, omega, sigma1, sigma2, delta = user.protocol_five(r, c, s1, s2, d)
    
    #print((((pow(user.h, ((user.UserKeypair.gamma)*s2) + user.t4, user.p))* pow(issuer.z2, (user.UserKeypair.gamma) * d, user.p))) % user.p == 
    #((pow(b2, user.UserKeypair.gamma, user.p)) * pow(user.h, user.t4, user.p)) % user.p
    #)
    #value1 = (pow(b2, user.UserKeypair.gamma, user.p) * pow(user.h, user.t4, user.p)) % user.p
    #value2 = (pow(user.h, sigma2, user.p) * pow(user.zeta2, d, user.p)) % user.p 
    
    #print(value1 == value2)
    
    #credential_tracing(xi, issuer.upsilon, xt, params)
    
#     print( % user.p == ( % user.p)) 
    
#     print((((pow(user.h, ((user.UserKeypair.gamma)*s2) + user.t4, user.p))* pow(issuer.z2, (user.UserKeypair.gamma) * d, user.p))) % user.p)