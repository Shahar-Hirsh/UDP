import socket
server_soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_soc.bind(('0.0.0.0',8888))

while True:
    data,client_address = server_soc.recvfrom(1024)
    print(f"client sent: {data.decode()}")
    try:
        server_soc.sendto(f"hello {data.decode()}".encode(),client_address)
    except Exception as e:
        break

server_soc.close()