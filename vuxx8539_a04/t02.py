"""
-------------------------------------------------------
Assignment 4 t02
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from Queue_array import Queue

source = Queue()
target = Queue()

source.insert(1)
source.insert(2)
source.insert(3)

target.insert(1)
target.insert(2)
target.insert(3)
target.insert(4)

equals = source == target

print(equals)
