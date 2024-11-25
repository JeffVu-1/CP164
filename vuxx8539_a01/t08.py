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
from functions import matrix_stats

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
small, large, total, average = matrix_stats(a)
print (small, large, total, average)
