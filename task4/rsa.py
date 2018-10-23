import binascii

def main():
	# select two primes
	P = 53
	Q = 59

	# calc public key
	n = P * Q
	print('n:', n)

	# select an exponenent
	e = 3
	print('e:', e)

	# calc phi(n)
	phi_n = (P - 1) * (Q - 1)
	print('phi_n:', phi_n)

	# calc private key
	k = 2
	d = (k * phi_n + 1) // e
	print('d:', d)

	# encrypt message

	# this whole section isn't working properly.
	# i don't understand how this example works: 
		# https://www.geeksforgeeks.org/rsa-algorithm-cryptography/
		# where is 8 and 9 coming from????? H = 72, I = 73 in ASCII

	# I feel like it's something to do with this:
		# enc is [pow(ord(char),key,n) for char in plaintext]
		# dec is [chr(pow(char, key, n)) for char in ciphertext]
	# but every implementation on the web does it differently

	m = b'HI'
	m_hex = binascii.hexlify(m)
	m_int = int(m_hex, 16)
	
	print('m:', m)
	print('m_hex:', m_hex)
	print('m_int:', m_int)
	assert m_int == 89 # FAIL

	c = pow(m_int, e, n)
	decrypted = pow(c, d, n)

	print('c:', c)
	print('decrypted:', decrypted)
	assert decrypted == c # FAIL

	unhex = binascii.unhexlify(decrypted)

	print('unhex:', unhex)
	assert unhex == m # FAIL

# TODO
def gcd(a, b):
	pass

# TODO
def multiplicative_inverse(e, phi):
	pass

if __name__ == '__main__':
	main()