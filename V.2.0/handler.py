# -*- coding: utf-8 -*-

import os 
import sys
sys.path.append('models/')
from listener import Listener
from logos import Logo
from time import sleep

def cleaning(name):
    os.system("clear")
    os.system("figlet {}".format(name ))

def main():
    cleaning("CONFIG LISTENER")
    listener = Listener(input("LHOST: "),input("LPORT: "))
    logo = Logo()
    os.system("clear")
    logo.printListener()
    opt = int(input("Enter your choice #~:  "))
    if opt >=1 and  opt<=5 :
        print("wait #)...")
        listener.initListener(opt)
    else:
        print("ELECCION ERRONEA")
        sleep(5)
        cleaning("BYE FRIEND #)")

        

