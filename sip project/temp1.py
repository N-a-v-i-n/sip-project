import socket

s=socket.socket()
print("Socket obj created")

s.bind((socket.gethostname(),56789))
s.listen(5)
print(f"listen....{socket.gethostname()}")
while True:
    client,port=s.accept()
    print("client connected : ",client,"and port is : ",port)
    client.send(("welcome to my server").encode())