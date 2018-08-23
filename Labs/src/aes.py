# ----------------------------------------
#
# Sample program to illustrate the use of pycrypto (pip install pycrypto)
#
# Needs to be modified to
#   [1] read a file in and write out the encrypted contents
#   [2] take an encrypted file and write out the plaintext version
#
# -----------------------------------------


import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

BLOCK_SIZE = 16

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

# Taking input and password export base64 encoded encrypted content

def encrypt(raw, password):

    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)

    return base64.b64encode(iv + cipher.encrypt(raw.encode("utf-8")))


# Taking encrypted base64 encoded input and password export decrypted content

def decrypt(enc, password):

    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)

    return unpad(cipher.decrypt(enc[16:]))


#----------------------------------------------------
# Program code - change after checking that it works
#----------------------------------------------------

password = input("Enter encryption password: ")

# First let us encrypt secret message

encrypted = encrypt("This is a secret message", password)

print(encrypted)
 

# Let us decrypt using our original password

decrypted = decrypt(encrypted, password)

print(bytes.decode(decrypted))
