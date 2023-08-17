import socket
host = "www.google.com"
try:
    addr=socket.gethostname(host)
    name=socket.gethostbyaddr("192.168.5.1")
    print("The ip address if the host {host} is: {addr}")
except:
    print("the website does not exits")