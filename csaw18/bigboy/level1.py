#!/usr/bin/python

import socket
import cPickle
import os
import sys
import signal

PORT = 54321
localhost = '127.0.0.1'

def handle(cs, addr):
	print "Conn from", addr
	cs.sendall("HAI\n")

	try:
		l = cPickle.loads(cs.recv(1024))
                print 'l is: ', l
		s = sum(l)
		cs.sendall("%d\n" % s)
	except Exception as e:
                print e
		cs.sendall("fail :(\n")


	cs.sendall("bye\n")
	cs.close()

signal.signal(signal.SIGCHLD, signal.SIG_IGN)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((localhost, PORT))
s.listen(100)


while 1:
	(cs, addr) = s.accept()
	pid = os.fork()

	if pid == 0:
		s.close()
		handle(cs, addr)
		sys.exit(0)

	cs.close()

