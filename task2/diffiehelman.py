import os
import sys
import json
from Crypto.Hash import SHA256
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
#Shared between Alice and Bob
p = 37
g = 5

p = int("B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371", 16)
g = int("A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28AD662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5", 16)

a = 4
#Alice computes and sends A over to Bob
A = pow(g, a, p)


b = 3
#Bob computes and sends Alice B
B = pow(g, b, p)

#Alice
s_Alice = pow(B, a, p)

#Bob
s_Bob = pow(A, b, p)

print(s_Alice)
print(s_Bob)
#print(bytes([s_Alice]))
#print(bytes([s_Bob]))

h = SHA256.new()
h.update(s_Alice.to_bytes(128, 'little'))
kA = h.hexdigest()[:16]
print(kA)

h = SHA256.new()
h.update(s_Bob.to_bytes(128, 'little'))
kB = h.hexdigest()[:16]
print(kB)
print(type(kA))
kA = bytes(kA, 'utf-8')
kB = bytes(kB, 'utf-8')

#AES CBS ENCODE with ALice's Key
m0 = b'Hi Bob!'
cipher = AES.new(kA, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(m0, AES.block_size))
iv = cipher.iv
ct = b64encode(ct_bytes)
print(ct)

#AES CBC DECODE with Bob's key
cipher = AES.new(kB, AES.MODE_CBC, iv)
ct = b64decode(ct)
pt = unpad(cipher.decrypt(ct), AES.block_size)
print("The message was: ", pt)
