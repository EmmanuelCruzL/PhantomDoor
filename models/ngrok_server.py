from pyngrok import ngrok,conf
from time import sleep
conf.get_default().config_path ="/home/rubickcuv/Documentos/Repositorios/PhantomDoor/config/config.yml"

class tunnel(object):

    def __init__(self):
        self._port = 5555



    @property
    def port(self):
        return self._port
    @port.setter
    def port(self,port):
        self._port = port

    def create_tunnel(self)->list:
        try:
            
            ngrok.connect(self._port,"tcp")
            tunnels = ngrok.get_tunnels()
            if len(tunnels) ==1:
                return tunnels[0].public_url.split(":")
            else:
                return tunnels[0].public_url.split(":")
        except Exception  as e:
            print(type(e).__name__)
            return None
    def stop_tunnel(self):
        try:
            ngrok.kill()
            print("Stopping tunnel..")
            sleep(1)
        except Exception as e:
            print(type(e).__name__)
    
    def tunnel_log(self):
        #conf.get_default().log_event_callback = log_event_callback
        pass

if __name__ == "__main__":
    vpn = tunnel()
    
    ip = vpn.create_tunnel()
    print(ip[1].replace('/',''))
    sleep(10)
    vpn.stop_tunnel()






