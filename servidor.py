#servidor
from socket import *

host = gethostname()
port = 70000

print(f'HOST: {host}, PORT {port}')

serv = socket(AF_INET, SOCK_STREAM)
serv.bind((host, port))
serv.listen(5)

while 1:
  con, adr = serv.accept()
  while 1:
    msg = con.recv(1024)
    print(msg.decode())