#!/usr/bin/python
from pwn import *

def solve_x(question):
    # I have no idea why, but this only works by importing it into here
    import operator 
    #luckily division is never used
    inverse_of = { "-":"+", "+":"-", "*":"/", "/":"*" }
    ops = { "-":operator.sub, "+":operator.add, "*":operator.mul, "/":operator.div }
    tokens = question.split()
    operator = tokens[1]

    if tokens[0] == 'X':

        # Return inverse of the operator applied to the numbers that aren't X
        return ops[inverse_of[operator]](float(tokens[4]),float(tokens[2]))
    else:
        if operator == '+':
            return ops['-'](float(tokens[4]),float(tokens[0]))
        elif operator == '-':
            return -1 * ops['-'](float(tokens[4]),float(tokens[0]))
        elif operator == '*':
            return ops[inverse_of['*']](float(tokens[4]),float(tokens[0]))

    return 'ERROR: CASE NOT HIT!'

# Deal with ((((8 + X) + (5 - 9)) * ((9 * 8) - (7 + 16))) - (((11 - 16) - (2 + 2)) + ((19 * 14) - (16 + 11)))) * ((((16 - 4) + (15 - 8)) - ((8 - 1) + (16 - 6))) - (((12 - 11) * (2 - 2)) -
#((13 * 12) + (18 - 20)))) = 109356
ridiculous = "((((8 + X) + (5 - 9)) * ((9 * 8) - (7 + 16))) - (((11 - 16) - (2 + 2)) + ((19 * 14) - (16 + 11)))) * ((((16 - 4) + (15 - 8)) - ((8 - 1) + (16 - 6))) - (((12 - 11) * (2 - 2)) - ((13 * 12) + (18 - 20)))) = 109356"

for i, c in enumerate(ridiculous):
    if c is "(":
        temp_i = i+1
        while ridiculous[temp_i] is not ")":
            # If there are expressions nested within, skip
            if ridiculous[temp_i] is "(": 
                break
        else: 
            # Kind of wonky, if the while loop does not finish, go to the next iteration of for loop
            continue
        


r=remote("misc.chal.csaw.io", 9002)
r.recvuntil("**********************************************************************************")
while True:
    r.recvline() #whitespace
    q=r.recvline()
    print q
    r.recv(len("What does X equal?: ")) # prompt
    ans = solve_x(q)
    print ans
    r.send(str(ans)+'\n')
    r.recvuntil('YAAAAAY keep going')

r.close()
