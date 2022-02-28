
import socket
import multiprocessing
import numpy as np
from functools import partial


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

    HOST = '1.1.1.3'

    iterator = np.array([0]*100000)
    for i in range(100000):
        iterator[i] = i
    #outdata = bytes(rawInput,'utf-8')
        
    
    checkport_part = partial(checkPort, ip = HOST)
    results = pool.map(checkport_part,iterator)
    filtered_results = []
    for i in range(len(results)):
        if(results[i] != None):
            filtered_results.append(results[i])
    print(filtered_results)
    input("found these ports")


        #print('Received'+ repr(indata))