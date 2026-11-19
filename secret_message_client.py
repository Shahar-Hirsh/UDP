from scapy.all import *

ip='169.254.176.55'
while True:
    msg = input("enter a word to send or exit to stop: ")

    if msg.lower() != 'exit':
        checksum = 0
        counter = 1
        for letter in msg:
            checksum += ord(letter)
            my_packet = IP(dst=ip, id=counter) / UDP(dport=ord(letter))
            send(my_packet, verbose=0)
            counter += 1


        my_packet = IP(dst=ip) / UDP(dport=1, chksum = checksum)
        send(my_packet, verbose=0)

    else:
        break

print("bye bye")