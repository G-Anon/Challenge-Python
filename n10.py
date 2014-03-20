#!/usr/bin/env python

# 10. Password Generator

import random
import string

UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase
NUMBER = string.digits
SYMBOL = string.punctuation

def generator(length=8, upper=2, lower=2, number=2, symbol=2):
    prepass = []
    for i in range(0, upper):
        prepass.append(random.choice(UPPER))
    for i in range(0, lower):
        prepass.append(random.choice(LOWER))
    for i in range(0, number):
        prepass.append(random.choice(NUMBER))
    for i in range(0, symbol):
        prepass.append(random.choice(SYMBOL))
    random.shuffle(prepass)
    password = ''.join(prepass)
    return password

choice = ''
while (choice != '1') and (choice != '2'):
    print """
---------------------------------------------------------------------------
    Make a choice :
    1. Default (8 characters password)
    2. Specify your own length 
---------------------------------------------------------------------------"""
    choice = raw_input()
    if choice == '2':
        length = int(raw_input("Give length of password: "))
        temp = int(round(float(length)/4))
        upper = temp
        lower = temp
        number = temp
        symbol = length - 3*temp

if choice == '1':
    print "Your password is: ", generator()
if choice == '2':
    print "Your password is: ", generator(length, upper, lower, number, symbol)
