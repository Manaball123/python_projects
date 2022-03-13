
import socket
import multiprocessing
#from multiprocessing.dummy import Pool
import numpy as np
from functools import partial
import time

def checkPort(port,ip):
    global validports
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((ip, port))
            #s.sendall(outdata)
            #indata = s.recv(1024)
            #print('Received'+ repr(indata))
            #validports.append(port)
            print("VALID PORT FOUND. IT IS: " + str(port))
            return port
        except:
            print("port "+ str(port) + " is invalid")



if __name__ == "__main__":
    validports = []
    #rawInput = input("input data to send: ")
    poolSize = 60

    pool = multiprocessing.Pool(processes = poolSize)
    #pool = Pool(processes = poolSize)
    #pool = dummy.

    HOST = '10.7.180.29'

    iterator = np.array([0]*65536)
    for i in range(65536):
        iterator[i] = i
    #outdata = bytes(rawInput,'utf-8')
        
    
    checkport_part = partial(checkPort, ip = HOST)
    results = pool.map(checkport_part,iterator)
    filtered_results = []
    startTIme = time.time()
    for i in range(len(results)):
        if(results[i] != None):
            filtered_results.append(results[i])
    endTime = time.time()
    print("took " + str(endTime - startTIme) + " seconds to scan")
    print(filtered_results)
    input("found these ports")


        #print('Received'+ repr(indata))