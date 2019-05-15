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
    m = b'my msg'
    
    try:
      opts, args = getopt.getopt(sys.argv[1:],"hr:l:n:")
    except getopt.GetoptError:
        print ('parameter_test -r <round> -l <L> -n <N>')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
           print ('parameter_test -r <round> -l <L> -n <N>')
        elif opt in ("-r"):
           round = int(arg)
        elif opt in ("-l"):
           L = int(arg)
        elif opt in ("-n"):
           N = int(arg)
    
    
    sys.stdout = open('./result/parameter_test_output.txt', 'w')
    # prepare the params of 'p', 'q', 'g'
    total = 0
    
    for x in range(round):
        
        start = time.time()
        params = blindIssuing_version1.choose_parameters(L, N)
        # get the tracer 's public key 
        tracerKeypair = blindIssuing_version1.tracer_choose_keypair(params)
        tkey = tracerKeypair.yt
        xt = tracerKeypair.xt
        
        end = time.time()
        runtime = end - start
        msg = "{func} takes {time} second to complete"
        total = total + runtime
        
        print(msg.format(func= '[Parameter Generation]',
                             time=runtime))
    
    avg =  total / round
    amsg = "The average time is {time} second for {rounds} tests"
    print(amsg.format(time= avg, rounds=round))
    sys.stdout.close()