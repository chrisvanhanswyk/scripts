#!/usr/bin/python
# Author: Chris Van Hanswyk
# Purpose: To write hex characters to a file. This can make your 
# life easier when trying to write shellcode to a file.
# This works only in Python2!
# Usage example: python hexToFile.py 41414141 > file.bin
# Output: AAAA

import sys

sys.stdout.write(sys.argv[1].decode('hex'))