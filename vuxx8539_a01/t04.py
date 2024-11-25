"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""

from functions import file_analyze

fv = open('testing.txt', 'r')
upp, low, dig, whi, rem = file_analyze(fv)
print(upp, low, dig, whi, rem)
