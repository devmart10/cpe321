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
	m = 'hello world'
	c = []
	for letter in m:
		ct = pow(ord(letter), e, n)
		c.append(ct)
	print('c:', c)

	decrypted = []
	for ct in c:
		dt = chr(pow(ct, d, n))
		decrypted.append(dt)
	print('decrypted:', decrypted)

# TODO
def gcd(a, b):
	pass

# TODO
def multiplicative_inverse(e, phi):
	pass

if __name__ == '__main__':
	main()