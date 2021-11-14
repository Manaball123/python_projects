import socket

HOST = '123.117.164.217'  
PORT = 62312    
while True:
    rawInput=input("input data to send: ")

    outdata=bytes(rawInput,'utf-8')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(outdata)
        indata = s.recv(1024)

    print('Received'+ repr(indata))


