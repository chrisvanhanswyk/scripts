#!/usr/bin/python3
# Author: Chris Van Hanswyk
# Purpose: Decrypts a hex string that has been XOR'd using a one-character key
# Usage example: python3 xor.py

import binascii

# Example hex string: 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
encoded = binascii.unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
for xor_key in range(256):
    decoded = ''.join(chr(b ^ xor_key) for b in encoded)
    if decoded.isprintable():
        print(xor_key, decoded)