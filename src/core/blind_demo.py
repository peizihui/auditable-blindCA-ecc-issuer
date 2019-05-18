#author:rujia
#website:www.rujia.uk
#version:1.0

from charm.toolbox.ecgroup import ECGroup,G,ZR
from charm.toolbox.eccurve import secp160k1,secp192k1,secp256k1
from collections import namedtuple
import hashlib
from core import until


Parameters = namedtuple('Parameters', ['secp', 'group', 'g', 'h'])
IssuerKeypair = namedtuple('IssuerKeypair', ['x', 'y'])
UserKeypair = namedtuple('UserKeypair', ['gamma', 'xi'])
TracerKeypair = namedtuple('TracerKeypair', ['xt', 'yt'])

def choose_parameters_secp256k1():
    group = ECGroup(secp256k1)
    #g, h = group.random(G), group.random(G)
    g = until.point2Obj(14519509735293947827288577209312317083665953431108465511763141066544895460406, group)
    h = until.point2Obj(19684769395795572483620032515699151948010901016215908752425022930402275400968, group)
    parameters = Parameters(type, group, g, h)
    return parameters

def choose_parameters_secp192k1():
    group = ECGroup(secp192k1)
    #g, h = group.random(G), group.random(G)
    g = until.point2Obj(1428563551188986083161179061956749636445572091115567662998, group)
    h = until.point2Obj(1644171847129458040208599782211559882005427686467664482898, group)
    parameters = Parameters(type, group, g, h)
    return parameters

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
    def __init__(self, g, h, x, y, z, parameters):
        print("g0:", parameters.g)
        self.parameters = parameters
        self.g, self.h, self.z = g, h, z
        self.IssuerKeypair = IssuerKeypair(x, y)

    def protocol_two(self,yt,upsilon,zu,mu,s1,s2,d):
        
        print("g2:", self.parameters.g)
        z1 = yt ** upsilon
        z2 = zu * (z1 ** -1)
        a = self.parameters.g ** mu
        b1 = (self.parameters.g ** s1) * (z1 ** d) 
        b2 = (self.parameters.h ** s2) * (z2 ** d)
        
        return z1, z2, a, b1, b2

    def protocol_four(self, e, d, mu):
        print("g4:", self.parameters.g)
        c = e -  d
        r = mu - c * self.IssuerKeypair.x
        return r, c
    
    def protocol_six(self, xi, upsilon):
        return xi ** upsilon

class User:
    '''User U from the paper'''
    def __init__(self, g, h, z, gamma, xi, parameters):
        self.parameters = parameters
        self.g, self.h, self.z = g, h, z
        self.UserKeypair = UserKeypair(gamma, xi)
        
    def protocol_one(self,z,gamma):
        print("g1:", self.parameters.g)
        zu = z ** (gamma ** -1)
        return zu

    def protocol_three(self, z1, a, b1, b2, m, y, t1, t2, t3, t4, t5):
        print("g3:", self.parameters.g)
        zeta1 = z1 ** self.UserKeypair.gamma
        zeta2 = self.z * (zeta1 ** -1)
        alpha = (a * (self.parameters.g ** t1) * (y ** t2))
        beta1 = ((b1 ** self.UserKeypair.gamma) * (self.parameters.g ** t3) * (zeta1 ** t5))
        beta2 = ((b2 ** self.UserKeypair.gamma) * (self.parameters.h ** t4) * (zeta2 ** t5))
        epsilon = self.parameters.group.hash((zeta1, alpha, beta1, beta2, m), ZR)
        e =  epsilon - t2 - t5
        return zeta1, zeta2, alpha, beta1, beta2, epsilon, e 

    def protocol_five(self, r, c, s1, s2, d, t1, t2, t3, t4, t5):
        print("g5:", self.parameters.g)
        rho = r + t1
        omega = c + t2
        sigma1 = (self.UserKeypair.gamma * s1) + t3
        sigma2 = (self.UserKeypair.gamma * s2) + t4
        delta = d + t5
        return rho, omega, sigma1, sigma2, delta

def verify(rho, omega, delta, sigma1,sigma2, h, g, m, y, zeta1, zeta2, z, parameters):

    lhs = omega + delta

    tmp1 = ((g ** rho) * (y ** omega))
    tmp2 = (g ** sigma1 * zeta1 ** delta) 
    tmp3 = (h ** sigma2 * zeta2 ** delta) 
    
    print("tmp1", tmp1)
    print("tmp2", tmp2)
    print("tmp3", tmp3)

    rhs = parameters.group.hash((zeta1, tmp1, tmp2, tmp3, m),ZR)
    
    return lhs,rhs

