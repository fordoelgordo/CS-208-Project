#! /user/bin/env python3

# Server applicaiton to read a file "mydata.txt" from the local filesystem and send to a client

import socket
PORT = 65432                                    # Port to listen on
s = socket.socket()                             # Create a socket object
HOST = socket.gethostname()                     # Get the local machine name
s.bind((HOST, PORT))                            # Bind to the port
s.listen()                                      # Now wait for the client connection

print("Server application is listening for client connection...")

# Event loop
while True:
    conn, addr = s.accept() # Establish connection with client
    print("Connected by ", addr)
    data = conn.recv(1024) # Limit to 1024 bytes
    print("Server received", repr(data)) # Print data received by client

    # Server now opens the file on local filesystem to send to the client
    f = open("mydata.txt", 'rb') # Open file in binary
    l = f.read(1024) # Read 1024 bytes from the open file
    while l:
        conn.send(l)
        print('Sent ', repr(l)) # Print data sent
        l = f.read(1024) # Read the next 1024 bytes
    f.close()

    print("Done sending file to client")
    conn.close()
    break

s.close()
print("Closing socket connection")
