#!/usr/bin/python3
from . import OSC # no use yet to go and see OSC.py file in folder
import math # general python module
import socket

# IP = '127.0.0.1'
# HOST = 12002

def getOscSocket(ip,host, bufferSize = 1024): # initialise a socket at host@ip

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	if bufferSize!= 0:
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, bufferSize)
		print ('##### socket.SO_RCVBUF size set to', bufferSize, ' expect unprocessed packets drops \n ')


	try:
		sock.bind((ip, host))
		sock.setblocking(0)
		sock.settimeout(1e-5)
	except OSError as e:
		print ('###', e)
	return sock

def readSocket(sock):
		try:
			raw_msg = sock.recv(1024) # socket size

			if raw_msg:
				osc_msg = OSC.decodeOSC(raw_msg)

				out_msg = round(osc_msg[2],3)
				return out_msg

			else: return ()

		except socket.timeout: # nothing received
			return ()
		except OSError: # socket closed
			return ()
