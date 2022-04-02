
import socket
import multiprocessing
import numpy as np
from functools import partial
import os

def send(port,ip,payload):
    global validports
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            print("process " + str(os.getpid()) + " is trying to connect via "+ str(port))
            s.connect((ip, port))
            print("process " + str(os.getpid()) + " established a connection via "+str(port))
            s.sendall(payload)
            print("data might be sent through "+ str(port) + " by process " + str(os.getpid()) + ", the process should be listening for recieved data now")
            indata = s.recv(1024)
            print(" \n DATA RECIEVED: "+str(os.getpid()) + ' received: ||'+ repr(indata) +"|| via port "+ str(port) + "\n")
            return repr(indata)
        except:
            print("process " + str(os.getpid()) + " tried to do stuff with port "+ str(port) + ", but failed")



if __name__ == "__main__":
    validports = []
    rawPayload = ""
    payload = bytes(rawPayload,'utf-8')
    #rawInput = input("input data to send: ")
    poolSize = 10
    pool = multiprocessing.Pool(processes = poolSize)
    
    HOST = '51.161.134.100'
    ports = np.array([27015])

    """
    HOST = '1.1.1.3'
    ports = [100]
    """
    #outdata = bytes(rawInput,'utf-8')
        
    
    checkport_part = partial(send, ip = HOST, payload = payload)
    results = pool.map(checkport_part,ports)
    filtered_results = []
    for i in range(len(results)):
        if(results[i] != None):
            filtered_results.append(results[i])
    print(filtered_results)
    input("recieved some data here")


        #print('Received'+ repr(indata))