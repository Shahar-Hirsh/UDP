from scapy.all import *

conf.iface = "Npcap Loopback Adapter"

def MyFilter(p):
    """
    filters the message
    :param p: packet
    :return: if it is http
    :rtype: bool
    """
    return IP in p and p[IP].dst == '169.254.176.55' and UDP in p

def MyPrint(p):
    """
    prints the message
    :param p: packet
    :return: none
    """
    global checksum
    global msg
    global counter
    global correct_order


    if p[UDP].dport == 1:
        if correct_order:
            if checksum == p[UDP].chksum:
                print(msg)

        counter = 1
        correct_order = True
        checksum = 0
        msg = ''

    else:
        if counter != p[IP].id:
            correct_order = False

        checksum += p[UDP].dport
        msg += chr(p[UDP].dport)
        counter += 1


def MyStopFilter(p):
    """
    Checks if the sniffing should stop
    :param p: packet
    :return: True if sniffing should stop
    :rtype: bool
    """
    return stop_sniffing

checksum = 0
counter = 1
msg = ''
correct_order = True

p = sniff(iface="Npcap Loopback Adapter", lfilter=MyFilter, prn=MyPrint)

print("bye bye")