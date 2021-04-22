import socket                                         


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_ICMP)

host = "localhost"
port = 9999
message = "Coucou"

s.connect((host, port)) 
s.send(message.encode())
"""
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)       
output = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
ttl = 3
client.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
client.sendto('Coucou ping',(host,port))
output.bind((socket.gethostname(),0))
print 'receiving'
data, addr = output.recvfrom(5012)
print data
client.close()
output.close()"""