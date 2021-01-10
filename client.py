#! /user/bin/env python3

# Client application that receives the file from the server, and creates a copy on their local filesystem

# Define function to compute the checksum of a file
from hashlib import md5
def md5sum(filename):
    hash = md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(128 * hash.block_size), b""):
            hash.update(chunk)
    return hash.hexdigest()
orig_checksum = md5sum("mydata.txt")

# Now run the client code
import socket
s = socket.socket()
HOST = socket.gethostname()
PORT = 65432

s.connect((HOST, PORT))
s.send(b"Client connecting to server!")

# Client will now receive the file
with open('mydata_client_copy.txt', 'wb') as f:
    print("Creating file mydata_client_copy.txt")
    while True:
        # Receive the data froms server
        data = s.recv(1024)
        if not data:
            break
        # Write the data to file
        f.write(data)

f.close()
import hashlib
with open('mydata_client_copy.txt','rb') as file_check:
    file_hash = hashlib.md5()
    while chunk := file_check.read(8192):
        file_hash.update(chunk)

if orig_checksum == md5sum("mydata_client_copy.txt"):
    print("Copied files match")
else:
    print("Copied files do not match")
s.close()
print("Closing connection to server")

