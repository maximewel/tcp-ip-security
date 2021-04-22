import socket   
import os                                      


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.103"
port = 9999
message = "Coucou"

s.connect((host, port)) 
s.send(message.encode())