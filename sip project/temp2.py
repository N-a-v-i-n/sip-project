import socket

s=socket.socket()
s.connect((socket.gethostname(),56789))
msg=s.recv(1024)
print(msg.decode('utf-8'))