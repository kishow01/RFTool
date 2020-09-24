import time
import socket
from scapy.all import Dot11,Dot11Beacon,Dot11Elt,sendp,hexdump

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

netSSID = 'Jammer'

dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff',addr2='25:23:23:23:23:23', addr3='23:23:23:23:23:23')
beacon = Dot11Beacon(cap='ESS+privacy')
essid = Dot11Elt(ID='SSID',info=netSSID, len=len(netSSID))
rsn = Dot11Elt(ID='RSNinfo', info=(
'\x01\x00'
'\x00\x0f\xac\x02'
'\x02\x00'
'\x00\x0f\xac\x04'
'\x00\x0f\xac\x02'
'\x01\x00'
'\x00\x0f\xac\x02'
'\x00\x00'))
rsn = Dot11Elt(ID='RSNinfo', info=(
'\x01\x00'              #RSN Version 1
'\x00\x0f\xac\x02'      #Group Cipher Suite : 00-0f-ac TKIP
'\x02\x00'              #2 Pairwise Cipher Suites (next two lines)
'\x00\x0f\xac\x04'      #AES Cipher
'\x00\x0f\xac\x02'      #TKIP Cipher
'\x01\x00'              #1 Authentication Key Managment Suite (line below)
'\x00\x0f\xac\x02'      #Pre-Shared Key
'\x00\x00'))            #RSN Capabilities (no extra capabilities)

frame = dot11/beacon/essid/rsn
frame.show()
print("\nHexDump of frame:")
hexdump(frame)
raw_input("\nPress enter to start\n")




#SSID = 'JAMMER'
#sender = '23:23:23:23:23:23'

#dot11 = Dot11FCS(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff', addr2=sender, addr3=sender)
#beacon = Dot11Beacon()
#essid = Dot11Elt(ID='SSID', info=SSID, len=len(SSID))

#frame = dot11/beacon/essid

#frame.show()
#print("\nHexDump of frame:")
#hexdump(frame)
#raw_input("\nPress enter to start\n")
"""
while True:
    sock.sendto(bytes(frame), ('127.0.0.1', 52001))
    print('sending beacon frame...')
"""
f = open('tmp.txt', 'w')
f.write(bytes(frame))
f.close()

