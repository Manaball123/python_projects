import socket

HOST = '10.7.180.19'  
PORT = 135
while True:
    #rawInput=input("input data to send: ")
    rawInput = "hi"
    outdata = bytes(rawInput,'utf-8')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(outdata)
        indata = s.recv(1024)

    print('Received'+ repr(indata))


