from flask import session
from charm.core.engine.util import objectToBytes, bytesToObject
import binascii
from charm.toolbox.ecgroup import ECGroup,G,ZR


# tools
def getObjFromSession(key, group):
    value_bytes = session.get(key)
    orig_value = bytesToObject(value_bytes, group)
    return orig_value

def putBytesToSession(key, value, group):
    value_bytes = objectToBytes(value, group)
    session[key] = value_bytes
    
def point2Obj(x, group):
    temp_str = hex(x)[2:]
    dict_ecc = {708: 42,
               711: 48,
               714: 64}
    temp_str = (dict_ecc[group.groupType()] - len(temp_str)) * '0' + temp_str
    return group.encode(binascii.a2b_hex(temp_str), include_ctr=True)

def unmber2Obj(x, group):
    obj = group.init(ZR, x)
    return obj


import uuid
def get_mac_address(): 
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
    return "".join([mac[e:e+2] for e in range(0,11,2)])
