import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


target = input('Enter website or IP address to scan: ')


target_ip = socket.gethostbyname(target)
print('Scanning target:', target_ip)


def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False

start = time.time()


for port in range(10):
    if port_scan(port):
        print(f'port {port} is open')
    else:
        print(f'port {port} is closed')


end = time.time()
print(f'Time taken {end - start:.2f} seconds')