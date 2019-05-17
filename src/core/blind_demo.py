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
TracerKeypair = namedtuple('TracerKeypair', ['xt', 'yt'])

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
    return TracerKeypair(xt, yt)

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
        
        self.a = self.parameters.g ** self.mu
        
        self.b1 = (self.parameters.g ** self.s1) * (self.z1 ** self.d) 
        
        self.b2 = (self.parameters.h ** self.s2) * (self.z2 ** self.d)
        
        return self.z1, self.a, self.b1, self.b2

    def protocol_four(self, e):
        self.c = e -  self.d
        self.r = self.mu - self.c * self.IssuerKeypair.x
        return self.r, self.c, self.s1, self.s2, self.d
    
    def protocol_six(self, xi):
        return xi ** self.upsilon

class User:
    '''User U from the paper'''
    def __init__(self, g, h, gamma, xi, parameters):
        self.parameters = parameters
        self.g, self.h = g, h
        self.UserKeypair = UserKeypair(gamma, xi)
        
    def start(self, t1, t2, t3, t4, t5, z, y):
        self.t1, self.t2, self.t3, self.t4,self.t5 = t1, t2, t3, t4, t5
        self.z = z
        self.y = y
        
    def protocol_one(self):
        self.z_u = self.z ** (self.UserKeypair.gamma ** -1)
        return self.z_u

    def protocol_three(self, z1, a, b1, b2, m):
        self.zeta1 = z1 ** self.UserKeypair.gamma
        self.zeta2 = self.z / self.zeta1
        self.alpha = (a * (self.parameters.g ** self.t1) * (self.y ** self.t2))
        self.beta1 = ((b1 ** self.UserKeypair.gamma) * (self.parameters.g ** self.t3) * (self.zeta1 ** self.t5))
        self.beta2 = ((b2 ** self.UserKeypair.gamma) * (self.parameters.h ** self.t4) * (self.zeta2 ** self.t5))
        self.epsilon = self.parameters.group.hash((self.zeta1, self.alpha, self.beta1, self.beta2, m),ZR)
        self.e =  self.epsilon - self.t2 - self.t5
        return self.e

    def protocol_five(self, r, c, s1,s2, d):
        rho = r + self.t1
        omega = c + self.t2
        sigma1 = (self.UserKeypair.gamma * s1) + self.t3
        sigma2 = (self.UserKeypair.gamma * s2) + self.t4
        delta = d + self.t5
        return rho, omega, sigma1, sigma2, delta

def verify(rho, omega, delta, sigma1,sigma2, h,g,m, y, zeta1, zeta2,z, parameters):
    '''Signature verification'''
    lhs = omega + delta

    tmp1 = ((g ** rho) * (y ** omega)) 
    tmp2 = (g ** sigma1 * zeta1 ** delta) 
    tmp3 = (h ** sigma2 * zeta2 ** delta) 

    rhs = parameters.group.hash((zeta1, tmp1, tmp2, tmp3, m),ZR)
    
    return lhs,rhs

# tools
def getObjFromSession(key, group):
    value_bytes = session.get(key)
    orig_value = bytesToObject(value_bytes, group)
    return orig_value

def putBytesToSession(key, value, group):
    value_bytes = objectToBytes(value, group)
    session[key] = value_bytes

