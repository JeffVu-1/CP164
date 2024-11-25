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
from Sorts_List_linked import Sorts

list = [84, 66, 20, 27, 8, 12, 14, 35, 67, 29, 6, 10, 87, 2, 93, 39, 37, 69, 49]
Sorts.radix_sort(list)
for value in list:
    print(value, end=", ")

