from scapy.all import *

while True:
    msg = input("enter a word and exit to stop: ")

    for letter in msg:
        my_packet = IP(dst='192.168.4.91') / UDP(dport=ord(letter))
        send(my_packet, verbose=0)

    my_packet = IP(dst='192.168.4.91') / UDP(dport=8888)
    send(my_packet, verbose=0)

print("bye bye")