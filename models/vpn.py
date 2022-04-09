import openvpn_api  as vpn 

v =  vpn.VPN('localhost',7505)
v.connect()
# Do some stuff, e.g.
print(v.release)
v.disconnect()

