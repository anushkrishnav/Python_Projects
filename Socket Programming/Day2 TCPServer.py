#Server

import socket
s=socket.socket()
print("Server side socket sucessfully created")
# reserve a port on your computer 

#ports upto 2000 usually reserved for system purpose
port=12345
# bind to the port 
# we have not typed any ip in the ip field 
# instead we have used an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('127.0.0.1', port))
#USE 127.0.0.1 for local      
print ("socket binded to %s" %(port)) 
  
# put the socket into listening mode 
s.listen(5)      
print("socket is listening")            
  
# a forever loop until we interrupt it or  
# an error occurs 
while True: 
  
   # Establish connection with client. 
   c, addr = s.accept()      
   print ('Got connection from', addr )
  
   # send a thank you message to the client.  
   c.send(b"\n You connecteed with Anush Server \n\n Thank you for connecting\n") 
   
   # Close the connection with the client 
   c.close() 

