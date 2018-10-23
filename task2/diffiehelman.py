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

def main():
	# shared between Alice and Bob
	# p = 37
	# g = 5
	p = int("B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371", 16)
	g = int("A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28AD662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5", 16)

	# Alice picks large prime and computes A
	a = 7
	A = pow(g, a, p)

	# Bob picks large prime and computes B
	b = 3
	B = pow(g, b, p)

	# Alice creates a key
	k_Alice = create_key(B, a, p)

	# Bob creates a key
	k_Bob = create_key(A, b, p)

	# should be the same key
	assert k_Alice == k_Bob

	# share an iv between the two people
	shared_iv = os.urandom(16)

	# message 0
	m0 = b'Hi Bob!'

	# Alice encrypts a message for Bob
	m0_encrypted = cbc_encypt(m0, k_Alice, shared_iv)
	print('Alice sent:', m0)

	# Bob decrypts message from Alice
	m0_decrypted = cbc_decrypt(m0_encrypted, k_Bob, shared_iv)
	print("Bob received:", m0_decrypted)

	# message 1
	m1 = b'Hi Alice!'

	# Bob encrypts a message for Alice
	m1_encrypted = cbc_encypt(m1, k_Bob, shared_iv)
	print('Bob sent:', m1)

	# Alice decrypts message from Bob
	m1_decrypted = cbc_decrypt(m1_encrypted, k_Alice, shared_iv)
	print("Alice received:", m1_decrypted)

def cbc_encypt(message, key, iv):
	cipher = AES.new(key, AES.MODE_CBC, iv)
	padded = pad(message, AES.block_size)
	encrypted = cipher.encrypt(padded)
	encoded = b64encode(encrypted)
	return encoded

def cbc_decrypt(encrypted, key, iv):
	cipher = AES.new(key, AES.MODE_CBC, iv)
	decoded = b64decode(encrypted)
	decrypted = cipher.decrypt(decoded)
	unpadded = unpad(decrypted, AES.block_size)
	return unpadded

# returns an encoded key
def create_key(base, exp, mod):
	secret = pow(base, exp, mod)
	h = SHA256.new()
	h.update(secret.to_bytes(128, 'little'))
	h_key = h.hexdigest()[:16]
	b_key = bytes(h_key, 'utf-8')
	return b_key

if __name__ == '__main__':
	main()