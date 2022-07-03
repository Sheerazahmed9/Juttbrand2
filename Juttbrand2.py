#coding=utf-8

import os, sys, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    if not os.path.isfile('khosa.so'):

        os.system('curl -L https://github.com/Sheerazahmed9/Juttbrand2/blob/main/Baloch.cpython-310.so?raw=true -o Baloch.so')

        from Baloch import reg

        reg()

    else:

        from Baloch import reg

        reg()

elif bit == '32bit':

    if not os.path.isfile('Baloch.so'):

        os.system('curl -L https://github.com/Sheerazahmed9/Juttbrand2/blob/main/baloch.cpython-310.so?raw=true -o baloch.so')

        from baloch import reg

        reg()

    else:

        from baloch import reg

        reg()

