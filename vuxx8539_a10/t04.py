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
from Deque_linked import Deque
from Sorts_Deque_linked import Sorts

values = [84, 66, 20, 27, 8, 12, 14, 35, 67, 29, 6, 10, 87, 2, 93, 39, 37, 69, 49]
list = Deque()
for value in values:
    list.insert_rear(value)
Sorts.gnome_sort(list)
for value in list:
    print(value, end=", ")
