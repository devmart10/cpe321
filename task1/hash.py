# hash.py

import hashlib

def main():
    # loop until user terminates program
    while True:
        input_string = input()
        encrypted = encrypt(input_string)
        print(encrypted)

# expects a string
def encrypt(data_in):
    encrypted = hashlib.sha256(data_in.encode()).hexdigest()
    return encrypted

if __name__ == '__main__':
    main()
