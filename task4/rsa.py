import binascii
from Crypto.PublicKey import RSA

def main():
	# # select two primes
	# P = 53
	# Q = 59

	# # calc public key
	# n = P * Q
	# print('n:', n)

	# # select an exponenent
	# e = 3
	# print('e:', e)

	# # calc phi(n)
	# phi_n = (P - 1) * (Q - 1)
	# print('phi_n:', phi_n)

	# # calc private key
	# k = 2
	# d = (k * phi_n + 1) // e
	# print('d:', d)

	e = 65537
	bits = 2048
	key = RSA.generate(bits, e=e)
	P = key.p
	Q = key.q
	n = P * Q
	# d = key.d

	phi_n = (P - 1) * (Q - 1)
	inv = modinv(e, phi_n)
	d = pow(inv, 1, phi_n)

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

# """
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
# """

if __name__ == '__main__':
	main()