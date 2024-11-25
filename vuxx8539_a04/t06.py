"""
-------------------------------------------------------
Assignment 4 t06
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue

source = Priority_Queue()

source.insert(2)
source.insert(1)
source.insert(1)
source.insert(3)
source.insert(2)

target1, target2 = source.split_key(2)

print("Target 1: ")
while len(target1) > 0:
    print(target1.remove())

print("Target 2: ")
while len(target2) > 0:
    print(target2.remove())
