"""
-------------------------------------------------------
Assignment 4 t04 LowerLevel (in terms of coding like python vs c++)
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from Queue_array import Queue

source = Queue()

source.insert(1)
source.insert(2)
source.insert(3)
source.insert(4)

target1, target2 = source.split_alt()

print("Target 1: ")
while len(target1) > 0:
    print(target1.remove())

print("Target 2: ")
while len(target2) > 0:
    print(target2.remove())