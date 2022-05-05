from multiprocessing import Pool
import subprocess
import os


host = "localhost"
packet_size = 32768
processes = 50
packet_count = 1024
command = "ping" + " -n " + str(packet_count) + " -l " + str(packet_size) + " " + host

def ping(x):
    pid = str(os.getpid())
    while True:
        print("Process " + pid + " returned: " + str(subprocess.run(command,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode))

if __name__ == "__main__":
    with Pool(processes = processes) as pool:
        pool.map(ping, range(processes))




