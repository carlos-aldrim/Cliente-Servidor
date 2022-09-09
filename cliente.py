#cliente
from socket import *

host = gethostname()
port = 70000

cli = socket(AF_INET, SOCK_STREAM)
cli.connect((host, port))

while 1:
  msg = input("Digite:")
  cli.send(msg.encode())