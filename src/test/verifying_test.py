#author:rujia
#website:www.rujia.uk
#version:1.0

import sys
import time
import getopt
from core import blindIssuing_version1

if __name__ == '__main__':
    L, N = 1024, 160
    round = 10
   
    
    try:
      opts, args = getopt.getopt(sys.argv[1:],"hr:l:n:")
    except getopt.GetoptError:
        print ('verifying_test -r <round> -l <L> -n <N>')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
           print ('verifying_test -r <round> -l <L> -n <N>')
        elif opt in ("-r"):
           round = int(arg)
        elif opt in ("-l"):
           L = int(arg)
        elif opt in ("-n"):
           N = int(arg)
    
    def verifying_test(L,N,round):
        m = b'my msg'
        # prepare the params of 'p', 'q', 'g'
        params = blindIssuing_version1.choose_parameters(L, N)
        
        # get the tracer 's public key 
        tracerKeypair = blindIssuing_version1.tracer_choose_keypair(params)
        
        tkey = tracerKeypair.yt
        
        xt = tracerKeypair.xt
        
        sys.stdout = open('./result/verifying_test_output.txt', 'w')
        
        total = 0
        
        for x in range(round):
                   
            # start issing
            issuer = blindIssuing_version1.Issuer(params,tkey)
            issuer.start()
            user = blindIssuing_version1.User(params, issuer.IssuerKeypair.y,tkey)
            user.start()
            zu, xi = user.protocol_one()
            z1, a, b1, b2 = issuer.protocol_two(zu)
            e = user.protocol_three(z1, a, b1, b2, m)
            r, c, s1, s2, d = issuer.protocol_four(e)
            rho, omega, sigma1, sigma2, delta = user.protocol_five(r, c, s1, s2, d)
            # end issing
            
            start = time.time()
            blindIssuing_version1.verify(rho, omega, delta, sigma1, sigma2, user.h, m, user.y, user.zeta1,user.zeta2, user.z, params)
            end = time.time()
            runtime = end - start
            msg = "{func} takes {time} second to complete"
            total = total + runtime
            print(msg.format(func= '[Credential Verifying]',
                                 time=runtime))
        avg =  total / round
        amsg = "The average time is {time} second for {rounds} tests"
        print(amsg.format(time= avg, rounds=round))
        sys.stdout.close()