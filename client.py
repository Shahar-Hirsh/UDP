import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    data2send = input('enter msg to send or exit to stop - ')

    if data2send.lower() == "exit":
        break

    try:
        my_socket.sendto(data2send.encode(),('192.168.4.84',8888))
    except Exception as e:
        break

    data, remote_address = my_socket.recvfrom(1024)
    print(f"server sent: {data.decode()}")

my_socket.close()