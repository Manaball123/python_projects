from copy import deepcopy
from subprocess import DEVNULL
from sys import stdout
import iputils
import os
import subprocess
import multiprocessing

start = "10.7.128.0"
stop = "10.7.128.255"

num_packets = "1"

args = ["ping", "-n", num_packets]

def ping(ip):
    argv = deepcopy(args)
    argv.append(ip)
    response = subprocess.call(argv, stdout=DEVNULL, stderr = DEVNULL, stdin=DEVNULL)

    #and then check the response...
    if response == 0:
        print(ip + " responded")
        #ik garbage collection is a thing but i will still manually delete this
        del argv
        return ip
    else:
        #print(ip + "did not respond")
        return None

    
iplist = iputils.get_range_enum(start,stop)

def main():

    pool = multiprocessing.Pool(30)

    
    res = pool.map(ping,iplist)
    resl = list(filter(lambda item: item != None, res))

    print(resl)
    input("press enter to continue...")

    

if __name__ == "__main__":
    main()
    


    









