import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

UDP_IP = '192.168.0.1'
UDP_PORT = 50000
msg = bytes.fromhex('CC 80 80 80 80 00 00 33')
sock.sendto(msg, (UDP_IP, UDP_PORT))
sock.sendto(msg, (UDP_IP, UDP_PORT))
sock.sendto(msg, (UDP_IP, UDP_PORT))
sock.sendto(msg, (UDP_IP, UDP_PORT))
msg = bytes.fromhex('CC 82 7F 80 80 00 FD 33')
while True:
    sock.sendto(msg, (UDP_IP, UDP_PORT))
sock.clos
