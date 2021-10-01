# PhantomDoor
![scrot](https://github.com/EmmanuelCruzL/PhantomDoor/blob/master/assets/Phantom.jpg)

## ¿QUE ES PhantomDoor ?

PhantomDoor es una herramienta escrita en Python que nos permite obtener un sesión meterpreter para Windows, Linux, macOS, Android y web; incrustando un backdoor.


El funcionamiento es sencillo. Iniciamos el script; seleccionamos la plataforma objetivo (Windows, Linux, macOS, Android o web); se crea el archivo backdoor (.exe, .apk, .php, etc.) y se lo debemos pasar al víctima. Luego, abrimos una sesión de escucha esperando una conexión entrante. El resto será historia…

## INSTALACIÓN 

      sudo apt-get update
     
     
      sudo apt-get upgrade      
     
     
      sudo apt-get install python3`
     
     
      git clone  https://github.com/EmmanuelCruzL/PhantomDoor.git
## USO
     
      chmod +x PhantomDoor.py
     
      python3  PhantomDoor.py 
