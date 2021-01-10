import random
import string

# Set the random seed for reproducability
random.seed(123)

# Generate the random strings, and save to a file called mydata.txt
letters = string.ascii_letters
f = open('mydata.txt', 'w')
for j in range(200):
    f.write(''.join(random.choice(letters) for i in range(10)))
    f.write('\n')
f.write(''.join(random.choice(letters) for i in range(10)))
f.close()

# Compute the MD5 checkum and print it
# Define function to compute the checksum of a file
from hashlib import md5
def md5sum(filename):
    hash = md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(128 * hash.block_size), b""):
            hash.update(chunk)
    return hash.hexdigest()

print(md5sum("mydata.txt"))