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
import hashlib
with open('mydata.txt','rb') as file_check:
    file_hash = hashlib.md5()
    while chunk := file_check.read(8192):
        file_hash.update(chunk)

print(file_hash.hexdigest())