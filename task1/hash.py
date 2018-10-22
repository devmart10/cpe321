# hash.py
import hashlib
import sys

# user inputs part
def main1():
    # user input strings
    input1 = input('String 1:')
    input2 = input('String 2:')

    # encrypt them both using sha256
    encrypted1 = encrypt(input1)
    encrypted2 = encrypt(input2)

    # display hashed data
    print(encrypted1)
    print(encrypted2)

    # calc and show bit difference
    diff = calc_hamming(encrypted1, encrypted2)
    print('Different bits:', diff)

# finding collision part
def main2():
    # arg for bytes (2, 3, 4, ..., 12)
    num_bytes = int(sys.argv[1])
    d = {}
    a = 0
    no_collision = True
    while no_collision:
        a_hash = hashlib.sha256(bytes(a)).hexdigest()[:num_bytes]
        if a_hash in d:
            no_collision = False
            print(a, end='\t')
        else:
            d[a_hash] = a
            # print(a_hash, ':', a)
            a += 1

# expects a string
def encrypt(data_in):
    encrypted = hashlib.sha256(data_in.encode()).hexdigest()
    return encrypted

# calculate the Hamming distance of two inputs
# expects binary encoded data
def calc_hamming(a, b):
    # binary is complicated in python
    # simply get the binary digits of the inputs
    num_bits = max(len(a), len(b)) * 4
    a_bin = bin(int(a, 16))[2:].zfill(num_bits)
    b_bin = bin(int(b, 16))[2:].zfill(num_bits)

    # count differing bits
    count = 0
    for i in range(num_bits):
        if a_bin[i] != b_bin[i]:
            count += 1
    return count

if __name__ == '__main__':
    main2()
