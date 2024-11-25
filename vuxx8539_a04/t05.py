"""
-------------------------------------------------------
Assignment 4 t05
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue
from functions import pq_split_key

source = Priority_Queue()

source.insert(2)
source.insert(1)
source.insert(1)
source.insert(3)
source.insert(2)

target1, target2 = pq_split_key(source, 2)

print("Target 1: ")
while not target1.is_empty():
    print(target1.remove())

print("Target 2: ")
while not target2.is_empty():
    print(target2.remove())