'''import socket
s=socket.socket()
port=12345
s.bind(('',port))
print('socket binded to',port)
s.listen(5)
print('socket is listening')
while True:
    c, addr=s.accept()
    print('Got connection from',addr)
    c.send('Connected')
    c.close()

'''
import socket 
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname('www.google.com')
print (ip)