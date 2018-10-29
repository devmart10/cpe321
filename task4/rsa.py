import binascii
from Crypto.PublicKey import RSA

def main():
	# RSA settings
	e = 65537
	bits = 2048

	# generate two large primes
	key = RSA.generate(bits, e=e)
	P = key.p
	Q = key.q
	n = P * Q

	# calc public key
	phi_n = (P - 1) * (Q - 1)
	inv = multiplicative_inverse(e, phi_n)
	d = pow(inv, 1, phi_n)

	# encrypt message
	m = 'hello world'
	encrypted = []
	for letter in m:
		ct = pow(ord(letter), e, n)
		encrypted.append(ct)
	print('encrypted:', encrypted)

	# mallory plaintext attack
	plaintext = '2'
	cA = pow(ord(plaintext), e, n)
	cB = [cA * c for c in encrypted]

	decrypted = []
	for ct in encrypted:
		dt = chr(pow(ct, d, n))
		decrypted.append(dt)
	print('decrypted:', decrypted)


"""
Tried to implement ourselves, but ran out of time and decided to work on the other parts of the lab.
Citation: https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
"""
def gcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = gcd(b % a, a)
		return (g, x - (b // a) * y, y)

def multiplicative_inverse(a, m):
    g, x, y = gcd(a, m)
    return x % m
# end citation

if __name__ == '__main__':
	main()